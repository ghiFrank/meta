dictio = {1: 'one', 'number': 5}
dictio["two"] = 2
print(dictio[1])

dictio['number'] = 3
print(dictio)

del dictio['number']

for key, value in dictio.items():
    print(key,value)