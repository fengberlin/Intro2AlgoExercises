#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# extended bottom-up cut-rod
def Extended_bottom_up_cut_rod(p, n):
    '''
    p: the list of the price, if the length is i, then the price of this 'i' rod is p[i]
    n: the length of the rod
    s: s[i]: the first part cut of the length 'i' rod
    '''
    r = [-1 for i in range(n + 1)]
    s = [-1 for i in range(n + 1)]
    r[0] = 0
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s

def Print_cut_rod_solution(p, n):
    r, s = Extended_bottom_up_cut_rod(p, n)
    print('Length ' + str(n) + ' rod: ', end='')
    while n > 0:
        print(s[n], end=' ')
        n = n - s[n]
    print()

if __name__ == '__main__':
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    for i in range(1, len(p)):
        Extended_bottom_up_cut_rod(p, i)
        Print_cut_rod_solution(p, i)