import re

#hand = open("regex_sum_42.txt")
hand = open("regex_sum_218188.txt")
total = 0
for line in hand:
    line = line.rstrip()
    line_total = 0
    lst = re.findall('[0-9]+', line)
    for num in lst:
        line_total = line_total + int(num)
    total = total + line_total
print(total)
