# 10. Write a program to find the sum of natural numbers up to n.

# Recursive
def SumNaturalsRecursive(x):
    if x == 0:
        return x
    else:
        return x + SumNaturalsRecursive(x - 1)


# No recursive
def SumNaturals(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

sumSize = int(input("Sum n naturals"))

print("Recursive sum: ",SumNaturalsRecursive(sumSize))

print("No recursive sum: ",SumNaturals(sumSize))

# with formula
print("Sum with formula: ",sumSize * (sumSize + 1) / 2)


