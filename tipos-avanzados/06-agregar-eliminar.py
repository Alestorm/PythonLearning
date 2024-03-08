mascotas = ["Wolfgang", "Pelusa,", "Pulga", "Felipe", "Pulga", "Chanchito"]

mascotas.insert(1,"Melvin")
mascotas.append("Cochinito")
print(mascotas)
mascotas.remove("Pulga")
mascotas.pop(1)
del mascotas[0]
mascotas.clear()

print(mascotas)