# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:55:20 2020

@author: ARMS COMPUTERS
"""

# Maximum Pairwise Product Algorithm

def swap(input_numbers,max_index, pos):
    get_numbers = input_numbers[pos], input_numbers[max_index]
    input_numbers[max_index], input_numbers[pos] = get_numbers
    return input_numbers

    
n_number = int(input())
input_numbers = [int(x) for x in input().split()]
assert(n_number == len(input_numbers))

index = 0
for i in range(index+1, n_number):
    if input_numbers[i] > input_numbers[index]:
        index = i

input_numbers = swap(input_numbers,index, len(input_numbers) - 1)

index = 0
for i in range(index+1, n_number-1):
    if input_numbers[i] > input_numbers[index]:
        index = i

input_numbers = swap(input_numbers,index, len(input_numbers) - 2)   
max_pairwise_product = input_numbers[n_number-1] * input_numbers[n_number-2]
print(max_pairwise_product)