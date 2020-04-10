# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:22:26 2020

@author: Abdul Wahid
"""

    
def fab_number_last_digit(n1, n2):
    if n2 >= n1:
        if n1 <= 1 and n2 <= 1:
            return n1

        previous = 0
        current = 1
        fab_sum = 0
        for counter in range(n2 + 1):
            if counter >= n1:
                fab_sum += previous
                
            previous, current = current, previous + current

        return fab_sum % 10

if __name__ == '__main__':
    num1, num2 = map(int, input().split())
    print(fab_number_last_digit(num1, num2))