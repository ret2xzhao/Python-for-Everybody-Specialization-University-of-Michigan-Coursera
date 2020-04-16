# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    new_line = line.rstrip()
    print(new_line.upper())
