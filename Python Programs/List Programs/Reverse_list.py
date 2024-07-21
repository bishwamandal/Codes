"""
This function takes user input of numbers and stores them in a list until 0 is entered.
It then prints the reverse of the list.
"""

list = []

while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    list.append(n)

print("Reserve of the list = ", list[::-1])