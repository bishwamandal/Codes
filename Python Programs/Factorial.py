"""
Calculate the factorial of a given number.
"""

num = int(input("Enter a number: "))
f = 1

for i in range(1, num + 1):
    f *= i

print(f"The factorial of {num} is {f}")