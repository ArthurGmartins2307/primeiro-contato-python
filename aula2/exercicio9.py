numeros = [1,2,3,4,5,6,7,'abc',8,9,10]

for i in numeros:
    if type(i) == str:
        numeros.remove(i)

print(numeros)