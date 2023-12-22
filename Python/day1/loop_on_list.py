num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

count = 0

for enu,n in enumerate(num_list):
    if n == 36:
        print("Number 36 found at position:{}".format(enu))
        break
    if n > 36:
        print("{} is over 36".format(n))
    else:
        print("{} is under 36".format(n))
    count += 1
print(count)