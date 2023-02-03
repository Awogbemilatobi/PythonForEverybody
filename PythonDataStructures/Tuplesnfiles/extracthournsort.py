"""a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon. sample line: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008. Once you have accumulated the counts for each hour, print out the counts, sorted by hour"""

name = input("Enter file:")

lst = list()
realhour = list()
counts = dict()
handle = open(name)
for line in handle:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        line = line.split()
        sline = line[5]
        hours = sline.split(":")
        realhour.append(hours[0]) #list of the hours
for line in realhour:
    counts[line] = counts.get(line, 0) + 1 #create dictionary and frequency
       
       


for k,v in counts.items():
    lst.append((k,v))
lst = sorted(lst)

for k,v in lst:
    print(k,v)
        
