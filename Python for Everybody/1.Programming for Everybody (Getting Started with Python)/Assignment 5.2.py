array = []

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        num_int = int(num)
    except:
        print("Invalid input")
    array.append(num_int)

largest = max(array)
smallest = min(array)
print("Maximum is", largest)
print("Minimum is", smallest)
