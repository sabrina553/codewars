def square_sum(numbers):
    #your code here
    temp = 0
    for i in numbers:
        temp += i**2
    return temp
def square_sum_best(numbers):
    return sum(x **2 for x in numbers)

print(square_sum([1, 2, 2]))
