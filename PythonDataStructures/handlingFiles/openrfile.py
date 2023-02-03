"""a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case"""

fname = input("Enter file name: ")
with open(fname, 'r') as fh:
    for line in fh:
        h = line.upper().rstrip()
        print(h)
