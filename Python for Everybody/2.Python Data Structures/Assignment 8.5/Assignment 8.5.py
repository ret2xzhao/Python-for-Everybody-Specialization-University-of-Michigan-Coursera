fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

count = 0
for line in fh:
        line_rstrip = line.rstrip()
        line_split = line.split()
        if len(line_split) < 3 or line_split[0] != "From":
            continue
        print(line_split[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
