import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

html = urllib.request.urlopen(address, context=ctx).read()

dic = json.loads(html)
comments = dic['comments']
print(comments)

total = 0
for item in comments:
    total = total + item['count']
print(total)
