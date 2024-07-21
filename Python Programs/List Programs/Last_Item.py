"""
This program prompts the user to enter numbers until they enter 0. 
It then stores the numbers in a list and prints the last item in the list.
"""

list = []

while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    list.append(n)

print("Last item in the list = ", list[-1])