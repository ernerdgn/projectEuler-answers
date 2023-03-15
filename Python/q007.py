# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import sympy

num = 2
counter = 0

while True:
    if counter == 10001:
        print(num - 1)
        break

    if sympy.isprime(num):
        num += 1
        counter += 1

    else:
        num += 1
