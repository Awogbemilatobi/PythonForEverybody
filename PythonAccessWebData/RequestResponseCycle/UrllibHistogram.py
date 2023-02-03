"""program that accesses a text file on the web, and creates a dictionary that shows the frequency of each word in the file."""

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

for k,v in counts.items():
    print(k,v)
