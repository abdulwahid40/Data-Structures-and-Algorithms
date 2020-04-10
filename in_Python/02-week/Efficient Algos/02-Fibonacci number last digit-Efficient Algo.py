# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:35:24 2020

@author: ARMS COMPUTERS
"""

def fab_number_last_digit(n):
    if n <= 1:
        return n
    else:
        previous = 0
        current = 1
        for counter in range(n-1):
            remainder = previous + current
            remainder = remainder % 10
            previous, current = current, remainder
    
    return current
    


if __name__ == '__main__':
    number = int(input())
    print(fab_number_last_digit(number))