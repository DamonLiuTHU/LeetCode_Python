# encoding:utf8


def solve(n):
    if n <= 1:
        return 0
    re = 0
    while n > 1:
        if n == 2:
            re += 1
            break
        if n == 3:
            re += 2
            break
        elif (n % 2) == 1:
            re += 2
            n = (n-1) / 2
        else:
            re += 1
            n = n / 2
    return re


if __name__ == '__main__':
    N = int(input())
    print solve(N)
