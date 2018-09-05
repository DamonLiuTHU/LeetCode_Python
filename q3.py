#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(N, arr, d):
    sum, MAX = 0, 0
    for i in range(N):
        sum = sum + arr[i]
        MAX = max(MAX, sum)
        if sum >= d:
            return i + 1
    if sum <= 0:
        return -1

    t = (d - MAX + sum - 1) / sum
    re = t * N
    current = t * sum

    for i in range(N):
        current += arr[i]
        if current >= d:
            return re + i + 1


if __name__ == '__main__':
    n, d = [int(s) for s in raw_input().split(" ")]
    a = [int(s) for s in raw_input().split(" ")]
    print solve(n, a, d)
