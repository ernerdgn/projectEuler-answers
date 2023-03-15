# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_palindrome():
    temp = []
    
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            possible_ans = i * j
            str_of_num = str(possible_ans)
            length_of_num = len(str_of_num)
            
            for index in range(0, length_of_num):
                if index > length_of_num - 1 - index:
                    temp.append(possible_ans)
                
                if str_of_num[index] != str_of_num[length_of_num - 1 - index]:
                    break
                else:
                    continue
    
    ans = max(temp)
    #print(len(temp))  #5917
    return ans

print(largest_palindrome())
        
