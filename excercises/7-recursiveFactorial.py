# 7. Calculate the factorial of a number using recursion.

def factorial(x):
    if x == 1 :
        return 1
    else:
        return(x * factorial (x-1))


n = int(input("Enter a number"))
f = factorial(n)
print(f"{n}! = {f}")

