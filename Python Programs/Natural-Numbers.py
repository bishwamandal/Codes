"""
Prints the first n natural numbers.
"""

n = int(input("Enter the value of n: "))

print("The first", n, "natural numbers are: ")
for i in range(1, n + 1):
    print(i, end=", ")