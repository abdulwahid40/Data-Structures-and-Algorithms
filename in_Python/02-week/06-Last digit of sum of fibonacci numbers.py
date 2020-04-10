# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:22:26 2020

@author: Abdul Wahid
"""


def last_digit_fab_sum(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    fab_sum = 0
    for _ in range(n-1):
        previous, current = current, previous + current
        fab_sum += current
        
    return (fab_sum + 1) % 10

if __name__ == '__main__':
    number = int(input())
    print(last_digit_fab_sum(number))