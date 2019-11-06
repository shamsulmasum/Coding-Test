# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 00:03:10 2019

@author: shamsul
"""

def calculate_sum_square_difference(n):
    """ sum square difference """
    sum = (n * (n + 1)) / 2
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6
    return int((sum ** 2) - sum_of_squares)

if __name__ == '__main__':
    print(calculate_sum_square_difference(100))