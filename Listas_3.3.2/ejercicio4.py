arr = list()
aux = ""
for i in range(1,4):
    name = str(input(f"Nombre {i}: "))
    arr.append(name)
for i in arr:
    if len(i) > len(aux):
        aux = i

print(f"Nombre mas grande es: {aux}")