# 5. Create a program to reverse a string.

message = "Reverse string"
print(message[::-1])

# with for loop
message2 = "Reverse string"
reverse = ""
for i in range(len(message2) - 1, -1, -1):
    reverse = reverse + message2[i]

print(reverse)

