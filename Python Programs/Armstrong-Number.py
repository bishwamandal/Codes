"""
This program checks whether a given number is an Armstrong number or not.
An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
"""

num = int(input("Enter a number: "))
temp = num
sum = 0

while num > 0:
    sum += (num % 10) ** 3
    num //= 10

if temp == sum:
    print("The number is an Armstrong number!")
else:
    print("The number is not an Armstrong number!")