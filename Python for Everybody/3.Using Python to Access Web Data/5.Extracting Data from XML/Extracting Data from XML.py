import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

html = urllib.request.urlopen(address, context=ctx).read()

tree = ET.fromstring(html)
lst = tree.findall('comments/comment')
print('User Count:', len(lst))

total = 0
for item in lst:
    print('Name:', item.find('name').text)
    print('Count:', item.find('count').text)
    total = total + int(item.find('count').text)
print('Total:', total)
