# encoding:utf8
import sys


def solve(n, e):
    my_map = dict()
    my_map[1] = 1.0
    for idx in range(1, n + 1):
        if idx not in my_map:
            continue

        if idx in e:
            tmp = len(e[idx])

            for p1, p2 in e[idx]:

                if p2 not in my_map:
                    my_map[p2] = 0.0
                my_map[p2] += my_map[p1] * 1.0 / tmp

    if n not in my_map:
        return 0.0

    return my_map[n]


def get_input():
    while True:
        try:
            h = sys.stdin.readline().strip('\r\n')
            h = list(filter(lambda x: len(x) > 0, h.split(' ')))
            n, m = [int(x) for x in h[:2]]
        except Exception:
            break
        edges = dict()
        for line_ind in range(m):
            cur_line = sys.stdin.readline().strip('\r\n')
            cur_line = list(filter(lambda x: len(x) > 0, cur_line.split(' ')))
            p1, p2 = [int(x) for x in cur_line[:2]]
            if p1 not in edges:
                edges[p1] = list()
            edges[p1].append([p1, p2])

        res = solve(n, edges)
        sys.stdout.write('{}\n'.format(res))


if __name__ == '__main__':
    get_input()
