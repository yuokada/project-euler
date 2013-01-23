#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


import math

primes = [2, 3, 5, 7, 11, 13, 17, 19]

def get_prime_factors(x):
    base = x
    results = []
    for pn in primes:
        while x % pn == 0:
            results.append(pn)
            x = x / pn
    return (base, x, results)

print get_prime_factors(2520)  # =>  (2520, 1, [2, 2, 2, 3, 3, 5, 7])
#help(reduce)
results = [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
print reduce(lambda a, b: a*b, results, 1)
