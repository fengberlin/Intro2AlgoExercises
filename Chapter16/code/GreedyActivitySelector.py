#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# O(n)
def Greedy_activity_selector(s, f):
    n = len(s) - 1
    A = ['a1']
    k = 1
    for m in range(2, n + 1):
        if s[m] >= f[k]:
            A.append('a%s' % m)
            k = m
    return A

if __name__ == '__main__':
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    activities = Greedy_activity_selector(s, f)
    print(activities)