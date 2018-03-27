#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# bottom-up cut-rod
def Bottom_up_cut_rod(p, n):
    '''
    p: the list of the price, if the length is i, then the price of this 'i' rod is p[i]
    n: the length of the rod
    '''
    r = [-1 for i in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]

if __name__ == '__main__':
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for i in range(1, len(p)):    
        max_profit = Bottom_up_cut_rod(p, i) 
        print(max_profit, end=' ')
    print()