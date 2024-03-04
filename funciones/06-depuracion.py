def larg(text):
    result = 0
    for _ in text:
        result += 1
    return result


l = larg("Hello world!")
print(l)
