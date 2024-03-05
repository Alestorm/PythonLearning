mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas)
print(mascotas[1])
mascotas[0] = "Bicho"
print(mascotas)

print(mascotas[0:3])
print(mascotas[-1])

print(mascotas[::2]) #salta 1 elemento, empezando desde i = 0
print(mascotas[1::2])  #salta 1 elemento, empezando desde i = 1

numeros = list(range(21))
print(numeros[::2])
print(numeros[1::2])