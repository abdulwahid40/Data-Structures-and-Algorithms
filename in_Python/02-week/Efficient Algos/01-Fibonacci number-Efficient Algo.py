# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:35:24 2020

@author: ARMS COMPUTERS
"""

def calculate_fab(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    
    for _ in range(n-1):
        previous, current = current, previous + current
        
    return current
        
number = int(input())
print(calculate_fab(number))