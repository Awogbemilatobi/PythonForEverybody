import re
"""read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers."""

fhand = input('Enter file name:')
handle = open(fhand, 'r')
stringlists = re.findall('[0-9]+', handle.read())
integerlist = [int(x) for x in stringlists]

print(sum(integerlist))


""" shorter version
fhand = input('Enter file name:')
handle = open(fhand, 'r')
print(sum( [int(x) for x in (re.findall('[0-9]+', handle.read()))]))"""
