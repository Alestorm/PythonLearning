# https://exercism.org/tracks/python/exercises/armstrong-numbers
# 12. Armstrong Numbers 
#     An Armstrong number is a number that is the sum of its own digits
#     each raised to the power of the number of digits.

number = input("Enter a number")
l = len(number)
sum = 0

for c in number:
    sum +=int(c)**l

print("Armstrong" if sum == int(number) else "Not Armstrong")

