punto = {"x": 25, "y": 50}
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)


if "lala" in punto:
    print("Encontré lala", punto["lala"])


print(punto.get("x"))
print(punto.get("lala", 97))

del punto["y"]

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor, punto[valor])
