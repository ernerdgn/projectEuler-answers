# 2520 is the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

all_divisors = []
for i in range (1,21):
    all_divisors.append(i)

def func():
    ans = 2520
    flag = False
    while True:
        c = 0
        for divisor in all_divisors:
            if ans % divisor != 0:
                break
            else:
                c += 1
                if c == len(all_divisors) - 1:
                    flag = True
                continue
        if flag:
            return ans
        else:
            ans += 20
            continue
    
print(func())
