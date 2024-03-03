n1 = input("First number: ")
n2 = input("Second number: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 +n2
resta = n1-n2
multi = n1*n2
div = n1/n2

mensaje = f"""Para los números {n1} y {n2}
el resultado de la suma = {suma}
el resultado de la resta = {resta}
el resultado de la multiplicación = {multi}
el resultado de la división = {div}
"""

print(mensaje)