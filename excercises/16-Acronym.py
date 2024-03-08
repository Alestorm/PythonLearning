# 16. Acronym 
# https://exercism.org/tracks/python/exercises/acronym

def acronym(word):
    acr = ""
    word = word.replace('-'," ")
    word = word.split()
    for char in word:
        acr += char[0]
    return acr.upper()

print(acronym("As Soon As Possible"))
