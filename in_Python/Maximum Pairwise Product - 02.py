# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:56:22 2020

@author: ARMS COMPUTERS
"""

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first+1, n):
            max_product = max(max_product, numbers[first] * numbers[second])
    
    return max_product

if __name__ == '__main__':
    number_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    assert(number_n == len(input_numbers))
    print(max_pairwise_product(input_numbers))

