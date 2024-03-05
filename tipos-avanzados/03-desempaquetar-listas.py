numeros = [1, 2, 3]

# está feo!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros

print(primero, segundo, tercero)

primero, *otros = numeros
print(primero,otros)