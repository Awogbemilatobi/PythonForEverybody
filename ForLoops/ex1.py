"""program that repeatedly reads numbrs until the user enters "done". once "done"
is entered, print out the total, count, and average of the numbers. if the user
enters anything other than a number, detect their mistake using try and except,
print a error message and skip to the next number"""

count = 0
sums = 0

while True:
    typein = input("Enter a number:")

    try:
        goat = int(typein)
        sums = sums + goat
        count = count + 1
    except:
         print("Bad data \nInvalid input")
    
    
    if typein == 'done':
        break
print(f"{sums}, {count}, {sums/count}")

