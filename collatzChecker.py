import math
n = int(input("Enter an integer"))
i = 0
while n > 1:
    if n % 2 == 0:
        n = n / 2
        i = i + 1
    else:
        n = n * 3 + 1
        i = i + 1

print(f"{i} steps for {n} to reach 1 using the Collatz algorithm")

        