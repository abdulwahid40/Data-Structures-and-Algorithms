# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:46:56 2020

@author: Abdul Wahid
"""


def fab_number_last_digit(n):
    if n <= 1:
        return n
    else:
        previous = 0
        current = 1
        fab_sum_squares = 0
        for _ in range(n-1):
            previous, current = current, previous + current
            fab_sum_squares += current ** 2

        return (fab_sum_squares + 1)  % 10

if __name__ == '__main__':
    number = int(input())
    print(fab_number_last_digit(number))