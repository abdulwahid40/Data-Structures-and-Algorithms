# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:48:19 2020

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
    for _ in range(n-1):
        previous, current = current, previous + current
        
    return current % m
    
    

if __name__ == '__main__':
    num, mod = map(int, input().split())
    print(fab_num_remainder(num, mod))