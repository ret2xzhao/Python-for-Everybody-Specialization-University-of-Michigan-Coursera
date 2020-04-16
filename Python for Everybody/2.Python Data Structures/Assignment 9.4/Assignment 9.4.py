fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

dic= {}
for line in fh:
        line_rstrip = line.rstrip()
        line_split = line.split()
        if len(line_split) < 3 or line_split[0] != "From":
            continue
        dic[line_split[1]] = dic.get(line_split[1], 0) + 1
        
count = -1
person = None
for key,value in dic.items():
    if value > count:
        count = value
        person = key

print(person, count)
