
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter url: ')
print('Retrieving', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)# accessing the url using urllib
data = uh.read()# reading the url content using the read function
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)# parses xml data 
lst = tree.findall('comments/comment')#find the comment tag inside the comments tag

for item in lst:
    count = count + 1
    t = item.find('count').text
    total = total + int(t)

print('Count:', count)
print('Sum:', total)
