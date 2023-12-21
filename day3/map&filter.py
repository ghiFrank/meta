menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

#normal loop
def C_only(listo):
    for coffee in listo:
        if coffee[0] == 'c':
            print(coffee)
C_only(menu)


def find_C(coffee):
    if coffee[0] == 'c':
        return coffee

#map:runs whole list through condition
mapL = map(find_C, menu)
for x in mapL:
    print(x)

#filter:same as map but creates new list with only true values
filterL = filter(find_C, menu)
for x in filterL:
    print(x)