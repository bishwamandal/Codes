"""
This program takes a list of numbers as input from the user, removes the first and last elements, and sorts the remaining elements in ascending order.
"""

list = []

while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    list.append(n)

list.pop(0)
list.pop(-1)
list.sort()

print("Sorted list (without first and last element): ", list)