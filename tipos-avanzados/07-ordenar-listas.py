numeros = [2, 3, 5, 8, 45, 74, 88, 9]

numeros.sort()  # affects the orignal list
print(numeros)

numeros.sort(reverse=True)
print(numeros)

numeros2 = sorted(numeros)  # new list
print(numeros2)

numeros2 = sorted(numeros, reverse=True)  # new list, doesn't affect the original
print(numeros2)

usuarios = [[4, "Lana"], [5, "Obsidia"], [1, "Liz"]]
print(usuarios)
usuarios.sort()
print(usuarios)

usuarios2 = [[ "Lana",4], ["Obsidia",5], ["Liz",1]]

def ordena(elemento):
    return elemento[1]

usuarios2.sort(key=ordena,reverse=True)
print(usuarios2)

usuarios3 = [[ "Lana",4], ["Obsidia",5], ["Liz",1]]
usuarios3.sort(key=lambda el:el[1])
print(usuarios3)