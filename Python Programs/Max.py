"""
This program prompts the user to enter five numbers and finds the biggest number among them.
"""

numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

biggest = max(numbers)

print("The biggest number is:", biggest)