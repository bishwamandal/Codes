num = int(input("Enter a number: "))

rev = 0
temp = num

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if num == rev:
    print("The number is a palindrome!")
else:
    print("The number is not a palindrome!")