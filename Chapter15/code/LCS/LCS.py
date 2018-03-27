#!/usr/bin/env python3
# -*-coding:utf-8-*-

# LCS_Length -> O(mn)
# print_LCS -> O(m + n)
# total: O(mn)

def LCS_Length(X, Y):
    c = [[0 for i in range(len(Y) + 1)] for i in range(len(X) + 1)]
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    # for i in range(len(X)):
    #     for j in range(len(Y)):
    #         if X[i] == Y[j]:
    #             c[i + 1][j + 1] = c[i][j] + 1
    #         else:
    #             c[i + 1][j + 1] = max(c[i + 1][j], c[i][j + 1])
    return c

def print_LCS(c, X, i, j):
    '''
    c: the length of the LCS between Xi and Yj
    i: the length of the X
    j: the length of the Y
    '''
    if i == 0 or j == 0:
        return
    if c[i][j] == c[i - 1][j - 1] + 1:
        print_LCS(c, X, i - 1, j - 1)
        print(X[i - 1], end='')
    elif c[i][j] == c[i - 1][j]:
        print_LCS(c, X, i - 1, j)
    else:
        print_LCS(c, X, i, j - 1)

if __name__ == '__main__':
    X = '10010101'
    Y = '010110110'
    c = LCS_Length(X, Y)
    print('\n'.join(str(row) for row in c))
    print_LCS(c, X, len(X), len(Y))
    print()