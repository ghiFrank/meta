listo = [1, 2 , 3 , 4]
print(*listo)
print(listo, sep = " ,")

listo.insert(len(listo), 5)
print(*listo)

listo.append(6)
print(*listo)

listo.extend([7, 8, 9])
print(*listo)

listo.pop(0)
print(*listo)

del listo[0]
print(*listo)

listo.remove(9)
print(*listo)

