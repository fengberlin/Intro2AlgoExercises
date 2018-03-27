#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# top-down with memoization
def Memoized_cut_rod(p, n):
    '''
    p: the list of the price, if the length is i, then the price of this 'i' rod is p[i]
    n: the length of the rod
    '''
    r = [-1 for i in range(n + 1)]
    return Memoized_cut_rod_aux(p, n, r)

def Memoized_cut_rod_aux(p, n, r):
    '''
    p: the list of the price, if the length is i, then the price of this 'i' rod is p[i]
    n: the length of the rod
    r: r[i] is the profit of the rod which length is i 
    '''
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1
        for i in range(1, n + 1):
            q = max(q, p[i] + Memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q

if __name__ == '__main__':
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for i in range(1, len(p) + 1):
        max_profit = Memoized_cut_rod(p, i)
        print(max_profit, end=' ')
    print()