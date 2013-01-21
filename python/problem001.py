#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

f = lambda x: x % 3 == 0 or x % 5 ==0

ls = [x for x in range(1000) if f(x)]
print sum(ls)
