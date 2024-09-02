# Next Prime Number - Have the program find prime 
# numbers until the user chooses to 
# stop asking for the next one.
# Strategies
# =========================================================
# to check if a number n is prime we can check for factors
# up until sqrt(n). if for all numbers between 2 - sqrt(n)
# n mod(num) = 0 
# then we add n to the list of primes

import math
limit = int(input("up to what digit would you like to find primes? "))
def generate_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    print(is_prime)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(limit**0.5) + 1):
        if is_prime[num]:
            for multiple in range(num*num, limit + 1, num):
                is_prime[multiple] = False

    return [num for num in range(2, limit + 1) if is_prime[num]]

# Example usage

prime_numbers = generate_primes(limit)
print(f"Prime numbers up to {limit}: {prime_numbers}")
        



    
