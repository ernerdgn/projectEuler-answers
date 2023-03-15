# Find the difference between the sum of the squares
# of the first one hundred natural numbers and the square of the sum.

numbers = []
for i in range(1,101):
    numbers.append(i)

def sum_square_difference():
    temp = 0
    sum_of_squares = 0
    for number in numbers:
        temp += number
        sum_of_squares += number ** 2
    square_of_sum = temp ** 2
    ans = abs(sum_of_squares - square_of_sum)
    return ans

print(sum_square_difference())