# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:46:56 2020

@author: Abdul Wahid
"""


def pisano_period(m):
    previous = 0
    current = 1
    for counter in range(0, m*m):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return counter + 1
    
    
def fab_num_remainder(n, m):
    pisano = pisano_period(m)
    n = n % pisano
    if n == 0:
        return n
    
    previous = 0
    current = 1
    total = 0
    for _ in range(n):
        total += current ** 2
        previous, current = current, previous + current
        
    return total % m
    
    

if __name__ == '__main__':
    num = int(input())
    mod = 10
    print(fab_num_remainder(num, mod))