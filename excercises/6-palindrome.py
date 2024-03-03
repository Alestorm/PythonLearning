# 6. Write a function to check if a string is a palindrome.
word = "radar"
reverseWord = word[::-1]

print(reverseWord)
print("Is palindrome" if word == reverseWord else "Not palindrome")

