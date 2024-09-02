# This program finds the prime factorisation of any integer
# Notes:
# A prime has no factors except for 1 and itself.
# To determine primeness, we can find all the primes up to a number
# Because we're looking for factors, we only need to look up to n/2.
# Once we have the primes in range(2, floor(n/2)) we check modular
# for all primes in our set we check n % prime == 0 
# if true add two factor set and divide n / prime
# for dividend, repeat process.
# output primes as products
import math
primes = []
n = int(input("enter a number silly!"))
candidates = list(range(2, math.floor(n/2)))
print(candidates)
for x in candidates:
    if x % 2 == 0:
        candidates.remove(x)
    elif x % 3 == 0:
        candidates.remove(x)
    elif x % 5 == 0:
        candidates.remove(x)
    elif x % 7 == 0:
        candidates.remove(x)
    else:
        for y in range(2, math.floor(n/2)):
            for x in candidates:
                if x % y == 0:
                    candidates.remove(x)
            
print(candidates)
