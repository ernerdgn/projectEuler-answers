# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# Note: Once the chain starts the terms are allowed to go above one million

def collatz_function(num):
    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1
    
def func():
    ans = 0
    max_chain_lenght = -1
    for i in range(1, 1000000):
        chain = []
        temp = i
        while True:
            chain.append(temp)
            temp = collatz_function(temp)
            if temp == 1:
                break
        if max_chain_lenght < len(chain):
            max_chain_lenght = len(chain)
            ans = i
    return ans

print(func())
        
