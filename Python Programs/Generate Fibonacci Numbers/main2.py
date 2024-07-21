n = int(input("Enter the value of n: "))

fn = [0, 1]

if n <= 2:
    fn = fn[:n]
else:
    for i in range(2, n):
        fn.append(fn[i-1] + fn[i-2])

print(f"The first {n} Fibonacci numbers are: {fn}")
