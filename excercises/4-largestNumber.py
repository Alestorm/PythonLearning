# 4. Write a function to find the largest of three numbers.

def FindLargest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    if num2 > num3 and num2 > num1:
        return num2
    else:
        return num3


n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))

print(f"The largest number is: {FindLargest(n1,n2,n3)}")

