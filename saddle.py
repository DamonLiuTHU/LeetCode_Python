def solution(A):
    def is_saddle(A, i, j):
        """
        count the saddle point number in matrix A.
        :param A: the input matrix with size MxN
        :param i: the first index
        :param j: the second index
        :return: if is saddle point or not
        """
        if not (0 < i < len(A) - 1 and 0 < j < len(A[0]) - 1):
            return False

        vertical_max = A[i][j] > A[i - 1][j] and A[i][j] > A[i + 1][j]
        vertical_min = A[i][j] < A[i - 1][j] and A[i][j] < A[i + 1][j]
        horizontal_max = A[i][j] > A[i][j - 1] and A[i][j] > A[i][j + 1]
        horizontal_min = A[i][j] < A[i][j - 1] and A[i][j] < A[i][j + 1]

        return (vertical_max and horizontal_min) or (
                vertical_min and horizontal_max)

    height = len(A)
    if height == 0:
        return 0
    width = len(A[0])
    if width == 0:
        return 0
    ans = 0

    for i in range(height):
        for j in range(width):
            ans += (1 if is_saddle(A, i, j) else 0)

    return ans


A = [[-2147483648, 2147483647, -2147483648],
     [-2147483648, 2147483646, -2147483648],
     [-2147483648, 2147483647, -2147483648], ]

print solution(A)