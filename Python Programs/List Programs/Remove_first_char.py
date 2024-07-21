"""
Removes the first character from each string in a list.
"""

list = []
modlist = []

while True:
    str = input("Enter a string (0 to stop): ")
    if str == "0":
        break
    list.append(str)

print("Original List = ", list)

for i in list:
    modlist.append(i[1:])

print("Modified List = ", modlist)