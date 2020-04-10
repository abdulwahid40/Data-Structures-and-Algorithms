# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:22:26 2020

@author: Abdul Wahid
"""


""" Calculating partial sum of fibonacci numbers from m to n
    Formula for calulating m to n 
    S(m,n) = F(n+2) - F(m+1) 
    If S(m,n) < 0 then remainder of -ve number is calulated according to 
    rules of -ve number remainder. 
    e.g. S(m,n) = -973 then -973 % 10 = -3 manually
    But it is actually equal to -3 = 7 mode 10 which is equal to 7
    in reality"""

def pisano_period(m):
    previous = 0
    current = 1
    for counter in range(0, m*m):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return counter + 1
        

def calculate_fab(n):
    if n <= 1:
        return n
    
    previous = 0
    current = 1
    
    for _ in range(n-1):
        previous, current = current, previous + current
        
    return current


def fab_sum_range(from_n, to_n, m):
    from_n = from_n + 1
    to_n = to_n + 2

    pisano = pisano_period(m)
    from_n = from_n % pisano
    to_n = to_n % pisano
    
    from_n = calculate_fab(from_n)
    to_n = calculate_fab(to_n)

    return (to_n - from_n) % 10



if __name__ == '__main__':
    from_num, to_num = map(int, input().split())
    mod = 10
    print(fab_sum_range(from_num, to_num, mod))