n = int(int(input("Enter the value of n: ")))

f1 = 0
f2 = 1
fn = 0

if n == 1:
    print(f1)
elif n == 2:
    fn == f2
else:
    for i in range(3, n + 1):
        fn = f1 + f2
        f1 = f2
        f2 = fn

print(f"The {n}th Fibonacci number is {fn}")