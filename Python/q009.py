# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
ans = 0
for a in range(1, 501):
    for b in range(1, 501):
        for c in range(1, 501):
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                ans = a * b * c
                print("a = ", a, ", b = ", b, ", c = ", c)
                print("ans = ", ans)
                break
        if ans != 0:
            break
    if ans != 0:
        break