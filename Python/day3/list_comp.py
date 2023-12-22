data = [2,3,5,7,11,13,17,19,23,29,31,31]

# updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

# creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0 ]
print("Divisible by four", fourx)

# Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("Nines: ", nines)

#use {} instead of [] to make a set
seto = {x for x in data}
print("Set:", seto)

#use () instead of [] to make a generator
gen_obj = (x for x in data)
for items in gen_obj:
    print(items, end = " ")