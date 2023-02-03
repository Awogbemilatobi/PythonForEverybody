"""reads file lines one by one, creates a dictionary of words and frequency(histogram)
and gets word with max number of occurence"""

name = input('Enter file name:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

#find the word with largest count
bigcount = 0
bigwordd = 0
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(f"word with highest occurence is {bigword} and occurs {bigcount} times")
