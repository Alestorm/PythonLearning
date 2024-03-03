# 9. Create a function to check if a number is prime.

def IsPrime(num):
    c = 0
    for i in range(1,num+1):
        if num % i == 0:
            print(i)
            c += 1
    return "Prime" if c == 2 else "Not prime"

number = int(input("Enter a number"))
print(IsPrime(number))

