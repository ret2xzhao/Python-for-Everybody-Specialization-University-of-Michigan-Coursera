fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)

dic= {}
for line in fh:
        line_rstrip = line.rstrip()
        line_split = line.split()
        if len(line_split) < 3 or line_split[0] != "From":
            continue
        hour = line_split[5][0:2]
        dic[hour] = dic.get(hour, 0) + 1

lst = []
for key,value in dic.items():
    newt = (key, value)
    lst.append(newt)
    
lst.sort()
for key,value in lst:
    print(key, value)
