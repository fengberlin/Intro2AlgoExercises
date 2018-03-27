#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# O(n)
def Recursive_activity_selector(s, f, k, n, result):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m = m + 1    # find the first activity in S_k to finish
    if m <= n:
        result.append('a%s' % m)  
        return Recursive_activity_selector(s, f, m, n, result)
    else:
        return None

if __name__ == '__main__':
    s = [0, 1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [0, 4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    result = []    # the result of the max subset of the S which contains n activities.
    Recursive_activity_selector(s, f, 0, 11, result)
    print(result)
