# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import sympy

ans = 0

for i in range(2, 2000000):
    if sympy.isprime(i):
        ans += i
    else:
        continue

print(ans)