# -*- coding: utf-8 -*-

def calculate_sum_square_difference(n):
    """ sum square difference """
    sum = (n * (n + 1)) / 2
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6
    return int((sum ** 2) - sum_of_squares)

if __name__ == '__main__':
    print(calculate_sum_square_difference(100))
    
#http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/runsums/triNbProof.html
#https://www.cs.odu.edu/~toida/nerzic/content/induction/example2/example2.html