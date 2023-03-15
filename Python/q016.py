# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

number = 2 ** 1000

def func(number):
    ans = 0
    for n in str(number):
        ans += int(n)
    return ans

print(func(number))
