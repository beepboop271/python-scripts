# meme script to download pictures of horses off google images
# and put it in a folder called the back so that you can have
# the horses in the back
import urllib
import urllib2
import re
import ssl

headers = {"User-Agent": "Mozilla/5.0"}
url = "https://www.google.com/search?q=horses&tbm=isch&safe=active"

request = urllib2.Request(url, headers=headers)
response = urllib2.urlopen(request)
page = response.read()
request = None
response = None

sslthing = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)

expr = re.compile(r"\"http([^\"]+)(\.jpg|\.png)")
matches = re.findall(expr, page)

for i in range(len(matches)):
    matches[i] = "http"+matches[i][0]+matches[i][1]

print "oh boy", len(matches)
for i in range(len(matches)):
    if i % 100 == 0:
        print i
    urllib.urlretrieve(matches[i], "the back/"+str(i)+matches[i][-4:], context=sslthing)
