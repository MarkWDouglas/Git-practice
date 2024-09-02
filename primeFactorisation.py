# This program finds the prime factorisation of any integer
# Pseudocode
# Goals: prime factorisation using a list filling with factors starting with a list
# from 2 -> sqrt(N)
# =====================================================================================
# receive input n
# while n mod(2) = 0
#   divide n by 2
#   add 2 to list of prime factors
# for odd from 3 -> sqrt(n)
#   while n mod(odd) = 0
#       add odd to list of prime factors
import math
 
# A function to print all prime factors of 
# a given number n
factors = []
def primeFactors(n):
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i and divide n
        while n % i== 0:
            factors.append(i)
            n = n / i
             
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        factors.append(int(n))
    print(" x ".join(map(str, factors)))
# Driver Program to test above function
 
n = int(input("Please enter an integer to be decomposed "))
primeFactors(n)