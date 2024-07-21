"""
Calculates the sum of the first n natural numbers.
"""

n = int(input("Enter the value of n: "))
sum = 0

for i in range(1, n + 1):
    sum += i

if n < 0:
    print("Enter a positive number!")
else:
    print(f"The sum of first {n} natural numbers is {sum}")
    