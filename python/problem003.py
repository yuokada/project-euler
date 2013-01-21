#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

def get_prime_factors(x):
    base = x
    results = []
    for pn in primes:
        while x % pn == 0:
            results.append(pn)
            x = x / pn
    return (base, x, results)

#print 5 * 7 * 13 * 29
t = 600851475143
p = 50000000
# get prime numbers
primes = [2]
for i in xrange(3, int(math.sqrt(p)), 2):
    res = [x for x in primes if i % x == 0]
    if not res:
        primes.append(i)

print get_prime_factors(t)
