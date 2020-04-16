fname = input("Enter file name: ")
fh = open(fname)

lst = []
for line in fh:
    line_strip = line.rstrip()
    line_split = line_strip.split()
    for word in line_split:
        if word in lst:
            continue
        else:
            lst.append(word)
lst.sort()
print(lst)
