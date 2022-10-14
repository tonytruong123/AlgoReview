# Big O Notation is used to measure how running time or space requirements 
# for program grow as input size grows

# RULES:

# Ex: time = a*n + b

# 1/ Keep the fastest growing term
# => time = a*n

# 2/ Drop constants
# time = O(n) (we drop the constant a)

# Ex:

################### O(n) ###################
def get_squared_numbers(numbers):
    squared_numbers = []
    for n in numbers:
        squared_numbers.append(n * n)
    return squared_numbers

numbers = [2,5,8,9]
print(get_squared_numbers(numbers))
# expected: [4,25,64,81] => O(n) => this function running time depends on the length of array numbers

################### O(1) ###################
def find_first_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe
# does not matter the length of the input 

##################O(n^2)################
numbers = [3,6,2,4,3]
duplicate = None
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break 
# => O(n^2) inner loop 

################# O(log n)##############
# Binary Search (search for a number in a sorted array)
# Find the middle element of an array 
# if the num < the middle => move the left point by previous mid point - 1
# if the num > the middle => move the right point by previous mid point + 1

# Explanation 
# we need to do the k iteration = n/ 2^k

