def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum
print(sum_of(5,6,8))

def sum_ofK(**kwargs):
    sum = 0
    for x, n in kwargs.items():
        sum += n
    return round(sum, 2)
print(sum_ofK(coffee=2.99, cake=4.55, juice=2.99))