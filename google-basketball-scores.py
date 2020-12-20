# Sketchy script to pull basketball scores from the google
# thingy for the 2019 nba finals, raptors v warriors
# PYTHON 2 (old lol)
import urllib2
import re
import time

headers = {"User-Agent": "Mozilla/5.0"}
url = "https://www.google.com/search?q=raptors+game&rlz=1C1CHBF_enCA722CA722&oq=raptors+game&aqs=chrome..69i57j69i60l5.1126j0j7&sourceid=chrome&ie=UTF-8#sie=m;/g/11h1m4tzw3;3;/m/05jvx;dt;fp;1;;"

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
page = response.read()

i = page.index("imso_mh__l-tm-sc imso_mh__scr-it")
s = page[i+20:i+200]
match = re.match(r"[^0-9]+([0-9]+)[^0-9]+([0-9]+)[^0-9]+", s)
g, r = map(int, match.group(1, 2))
print "g  r"
print g, r
gl = g
rl = r

while True:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    page = response.read()
    try:
        i = page.index("imso_mh__l-tm-sc imso_mh__scr-it")
        s = page[i+20:i+200]
        match = re.match(r"[^0-9]+([0-9]+)[^0-9]+([0-9]+)[^0-9]+", s)
        g, r = map(int, match.group(1, 2))
        if g-gl > 0:
            print g, r
            if g-gl == 3:
                print "unepic gamer moment"
        if r-rl > 0:
            print g, r
            if r-rl == 3:
                print "epic gamer moment"
        gl = g
        rl = r
    except(ValueError):
        print "error"

    time.sleep(1)
