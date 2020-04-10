# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:48:19 2020

@author: Abdul Wahid
"""


def fab_remainder(n,r):
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    
    for _ in range(n-1):
        previous, current = current, previous + current
    
    return current % r

if __name__ == '__main__':
    number, remainder = map(int, input().split())
    print(fab_remainder(number, remainder))