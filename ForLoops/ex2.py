"""program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number"""

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        num = int(num)
    except:
        print("Invalid input")
        continue
    if largest == None:
        largest = num
    elif largest < num:
        largest = num
    else:
        num = num
    if smallest == None:
        smallest = num
    elif smallest > num:
        smallest = num
    else:
        num = num
        
print("Maximum is", largest)
print("Minimum is", smallest)
