"""
This function prompts the user to enter numbers until they enter 0, and then returns the total number of items entered.
"""

list = []

while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    list.append(n)

print("Total number of items in the list = ", len(list))