"""
Prints all prime numbers up to the given value of n.
"""

n = int(input("Enter the value of n: "))

for i in range(2, n + 1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i, end=", ")