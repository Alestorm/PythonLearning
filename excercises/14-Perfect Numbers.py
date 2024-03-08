# 14 Perfect Numbers
# https://exercism.org/tracks/python/exercises/perfect-numbers
def classify(number):
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    if sum == number:
        return "Perfect"

    elif sum > number:
        return "Abundant"

    return "Deficient"


print(classify(number = int(input())))