"""
This program takes a number as input and calculates the decimal equivalent of fractions from 1/2 to 1/num.
"""

num = int(input("Enter a number: "))

for i in range(2, num + 1):
    print(f"1/{i} = {1/i}")