# 11. Write a simple calculator
print("Welcome to Calculator")
print("Write Close for exiting")
print("The operations are: + , - , * , /")

result = ""
while True:
    if not result:
        result = input("Enter number: ")
        if result.lower() == "close":
            break
        result = int(result)

    op = input("Enter operation: ")
    if op.lower() == "close":
        break
    n2 = input("Enter next number: ")
    if op.lower() == "close":
        break
    n2 = int(n2)

    if op.lower() == "+":
        result += n2
    elif op.lower() == "-":
        result -= n2
    elif op.lower() == "*":
        result *= n2
    elif op.lower() == "/":
        result /= n2
    else:
        print("Not valid operation")
        break

    print(f"Result: {result}")
