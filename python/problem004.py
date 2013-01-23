#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

palindromes = []
for x in xrange(999, 99, -1):
    for y in xrange(999, 99, -1):
        num = x * y
        num_r =  ''.join(reversed( [c for c in str(num)] ))
        if str(num) == num_r:
            palindromes.append(num)
print max(palindromes)
