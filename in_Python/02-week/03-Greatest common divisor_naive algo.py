# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:17:34 2020

@author: Abdul Wahid
"""


def gcd(a,b):
    current_gcd = 1
    for gcd in range(2, min(a,b) + 1):
        if a % gcd == 0 and b % gcd == 0:
            if gcd > current_gcd:
                current_gcd = gcd
                
    return current_gcd


if __name__ == '__main__':
    dividend, divisor = map(int, input().split())
    print(gcd(dividend,divisor))