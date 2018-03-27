#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def Fibonacci1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci1(n - 1) + Fibonacci1(n - 2)

def DP_Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a
    

if __name__ == '__main__':
    print(DP_Fibonacci(1))