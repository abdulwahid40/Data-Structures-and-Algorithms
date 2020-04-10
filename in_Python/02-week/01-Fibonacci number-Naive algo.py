# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:35:24 2020

@author: ARMS COMPUTERS
"""

def calculate_fab(n):
    if n <= 1:
        return n
    else:
        return calculate_fab(n-1) + calculate_fab(n-2)
        
        
number = int(input())
print(calculate_fab(number))