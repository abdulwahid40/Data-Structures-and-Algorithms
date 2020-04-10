# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:50:43 2020

@author: Abdul Wahid
"""


def lcm_naive(n1, n2):
    for lcm in range(1, n1*n2 + 1):
        if lcm % n1 == 0 and lcm % n2 == 0:
            return lcm
    
    return n1*n2


if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    print(lcm_naive(num1, num2))