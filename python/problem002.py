#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

fibo = [1,2]


index = 2
a = 1
x = 1
while a < 4000000:
    x += 1
    a = fibo[x-2] + fibo[x-1]
    fibo.append(a)

print sum([ x for x in fibo if x % 2 == 0])
