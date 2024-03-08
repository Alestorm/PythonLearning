usuarios = [["Lana", 4], ["Obsidia", 5], ["Liz", 1]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])

# print(nombres)

# nombres = [usuario[0] for usuario in usuarios]
# print(nombres)

# filtrar
# nombres = [usuario[0] for usuario in usuarios if usuario[1]>2]
# print(nombres)

# nombres = list(map(lambda usuario:usuario[0],usuarios))

menusUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menusUsuarios)
