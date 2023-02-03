"""a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475, Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below."""

# Use the file name mbox-short.txt as the file name
count = 0
total = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    a = line.find(" ")
    b = float(line[a+1:len(line)])
    count = count + 1 
    total = total + b
   
print(f"Average spam confidence: {total/count}")

