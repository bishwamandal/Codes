"""
Generates a list of 20 random numbers between 1 and 100.
Calculates the sum, average, maximum, minimum, second largest, second smallest, and count of even numbers in the list.
Prints the generated list and the calculated values.
"""

import random

list = []
sum = 0
avg = 0
even = 0

for i in range(20):
    num = random.randint(1, 100)
    list.append(num)
    sum += num
    avg = sum / 20
    mx = max(list)
    mn = min(list)
    if num%2 == 0:
        even += 1

print("List of 20 random numbers from 1 to 100:", list)
print("Sum of the list = ", sum)
print("Average of the list = ", avg)
print("Maximum number in the list = ", mx)
print("Minimum number in the list = ", mn)

list.sort()

print("Second Largest number in the list = ", list[-2])
print("Second Smallest number in the list = ", list[1])
print("Number of even numbers in the list = ", even)