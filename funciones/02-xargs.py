def sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)


sum(10, 3, 7, 3, 56, 99)
