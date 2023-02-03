"""program to lift a part/data from a string using find method"""

data = 'From stephen.marquard@uct.ac.za sat jan 5'
atpos = data.find('@')
print(atpos)
spacepos = data.find(' ', atpos) #next space after @
print(spacepos)
host = data[atpos+1 : spacepos] #info between @ and the next space
print(host)
