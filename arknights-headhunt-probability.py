# calculates binomial pdf for pulling from
# headhunting in the game arknights
# if you don't care about precision and
# accuracy you can change it from Decimals
# to floats, only makes a difference after like
# 10 decimal places lol
import itertools
import math
from decimal import Decimal

def get_P(count, base=Decimal("0.02"), accum=Decimal("0.02")):
    # get the probability of a success on the "count"th
    # attempt since the last success, with original
    # probability "base" and incrementing by "accum"
    # for each failure after 50 failures in a row
    if count <= 50:
        return base
    else:
        return min(Decimal(1), base+(accum*(count-50)))

def P(successes, n, p=Decimal("0.02"), accum=Decimal("0.02")):
    # get the probability of performing "n" pulls and
    # only getting successes at each pull number specified
    # in the list "successes" e.g. P([1, 6], 10) = probability
    # of success on the first and sixth attempt out of 10, i.e.
    # P(success AND fail AND fail AND fail AND fail AND success AND fail AND fail AND fail AND fail)
    successes = iter(successes)

    next_success = next(successes, -1)
    if next_success == 1:
        P = get_P(1, p, accum)
        count = 0
        next_success = next(successes, -1)
    else:
        P = 1-get_P(1, p, accum)
        count = 1

    for i in range(2, n+1):
        count += 1
        if i == next_success:
            P *= get_P(count, p, accum)
            count = 0
            next_success = next(successes, -1)
        else:
            P *= 1-get_P(count, p, accum)
    return P

def binompdf(trials, success, p=Decimal("0.02"), accum=Decimal("0.02")):
    # get the binomial pdf, the probability of getting
    # "success" successes out of "trials" trials
    # do note that this can get very slow, it has to
    # run through (trials choose success) combinations,
    # for example 70 trials and 5 success
    # = 70C5 combinations = 12 103 014 combinations
    prob = 0
    standard_p = (p**success)*((1-p)**(trials-success))

    if trials <= 50:
        # standard binompdf formula
        return math.comb(trials, success)*standard_p

    if success == 0:
        # definitly brute force
        return P([], trials, p, accum)

    # possible brute forcing of trial runs
    for l in itertools.combinations(range(1, trials+1), success):
        max_gap = l[0]
        for i in range(len(l)-1):
            max_gap = max(l[i+1]-l[i], max_gap)
        max_gap = max(trials-l[-1], max_gap)
        if max_gap > 50:
            # definitly brute force
            prob += P(l, trials, p, accum)
        else:
            # no need to brute force this time
            prob += standard_p
    return prob
