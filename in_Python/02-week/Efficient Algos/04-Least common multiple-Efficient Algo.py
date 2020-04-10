# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:50:43 2020

@author: Abdul Wahid
"""


import sys

def gcd(a,b):
    if b == 0:
        return a
        
    else:
        remainder = a % b
        return gcd(b, remainder)



if __name__ == '__main__':
    number1, number2 = map(int, input().split())
    if number1 > number2:
        print(int((number1*number2) / gcd(number1, number2)))
    else:
        print(int((number1*number2) / gcd(number1, number2)))
