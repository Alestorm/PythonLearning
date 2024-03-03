# 8. Write a program to generate Fibonacci series up to n terms.

# Recursive
n = int(input("Size of the fibonacci series: "))

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

for i in range(n):
    print(fibonacci(i))

# No recursive
print()
a, b = 0, 1
for i in range(n):
    print(a)
    f = a + b
    a = b
    b = f

