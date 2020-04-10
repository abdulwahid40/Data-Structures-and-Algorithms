# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:17:34 2020

@author: Abdul Wahid
"""

import sys

def gcd(a,b):
    if b == 0:
        print(a)
        sys.exit()
        
    else:
        remainder = a % b
        gcd(b, remainder)


if __name__ == '__main__':
    dividend, divisor = map(int, input().split())
    if dividend > divisor:
        gcd(dividend, divisor)
    else:
        dividend, divisor = divisor, dividend
        gcd(dividend, divisor)