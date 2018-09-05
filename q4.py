#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function, division


class TreeNode(object):
    left, right = 0, 0
    curr_sum, max_sum = 0, 0
    left_sum, right_sum = 0, 0


def build(tree, root, arr, left, right):
    # print(root)
    tree[root].left, tree[root].right = left, right
    if left == right:
        tree[root].curr_sum, tree[root].max_sum = arr[left], arr[right]
        tree[root].left_sum, tree[root].right_sum = arr[left], arr[right]
    else:
        mid = (left + right) >> 1
        left_child = root * 2
        right_child = root * 2 + 1
        build(tree, left_child, arr, left, mid)
        build(tree, right_child, arr, mid + 1, right)
        tree[root].curr_sum = tree[left_child].curr_sum + tree[
            right_child].curr_sum
        tree[root].max_sum = max(max(tree[left_child].max_sum,
                                     tree[right_child].max_sum),
                                 tree[left_child].right_sum + tree[
                                     right_child].left_sum)
        tree[root].left_sum = max(tree[left_child].left_sum,
                                  tree[left_child].curr_sum + tree[
                                      right_child].left_sum)
        tree[root].right_sum = max(tree[right_child].right_sum,
                                   tree[right_child].curr_sum + tree[
                                       left_child].right_sum)


def query(tree, root, left, right):
    if tree[root].left >= left and tree[root].right <= right:
        return tree[root]
    else:
        mid = (tree[root].left + tree[root].right) >> 1
        left_child = root * 2
        right_child = root * 2 + 1
        if right <= mid:
            return query(tree, left_child, left, right)
        elif left > mid:
            return query(tree, right_child, left, right)

        k1 = query(tree, left_child, left, mid)
        k2 = query(tree, right_child, mid + 1, right)

        ans = TreeNode()
        ans.curr_sum = k1.curr_sum + k2.curr_sum
        ans.max_sum = max(max(k1.max_sum, k2.max_sum),
                          k1.left_sum + k2.right_sum)
        ans.left_sum = max(k1.left_sum, k1.curr_sum + k2.left_sum)
        ans.right_sum = max(k2.right_sum, k2.curr_sum + k1.right_sum)
        return ans


if __name__ == '__main__':
    n, q = [int(s) for s in raw_input().split(" ")]
    a = [int(s) for s in raw_input().split(" ")]
    a = [0] + a
    queries = []
    for i in range(q):
        l, r = [int(s) for s in raw_input().split(" ")]
        queries.append((l, r))
    ans = [0] * q

    tree = [TreeNode() for _ in range(n * 4 + 1)]
    build(tree, 1, a, 1, n)
    for i in range(q):
        l, r = queries[i]
        qa = query(tree, 1, l, r)
        ans[i] = max(ans[i], qa.max_sum)

    a = [-x for x in a]
    tree = [TreeNode() for _ in range(n * 4 + 1)]
    build(tree, 1, a, 1, n)
    for i in range(q):
        l, r = queries[i]
        qa = query(tree, 1, l, r)
        ans[i] = max(ans[i], qa.max_sum)

    for x in ans:
        print(x)
