import collections


# def minWindow(s, t):
#     need, missing = collections.Counter(t), len(t)
#     i = I = J = 0
#     for j, c in enumerate(s, 1):
#         missing -= need[c] > 0
#         need[c] -= 1
#         if not missing:
#             while i < j and need[s[i]] < 0:
#                 need[s[i]] += 1
#                 i += 1
#             if not J or j - i <= J - I:
#                 I, J = i, j
#     return s[I:J]





def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    left = 0
    I, J = 0, 0
    need = collections.Counter(t)
    missing_num = len(t)

    for idx, char in enumerate(s):
        missing_num -= need[char] > 0
        need[char] -= 1

        if missing_num == 0:
            right = idx + 1
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            if J == 0 or right - left <= J - I:
                I, J = left, right
    return s[I:J]


S = "ADOBECODEBANC"
T = "ABC"
print(minWindow(S, T))