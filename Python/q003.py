# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import sympy

number = 600851475143

def largest_prime_factor(number):
    factor = 2
    num = number
    r = 2
    while True:
        if r < 2:
            break

        if num % factor == 0:
            r = num / factor
            num = r
            continue
        else:
            factor += 1
            if sympy.isprime(factor):
                continue
    return factor

print(largest_prime_factor(number))