def solution(A):
    """
    found number of countries in matrix A
    :param A:
    :return:
    """

    MIN = -1000000001  # define constant MIN
    # begin boundary case check
    N = len(A)
    if N == 0:
        return 0
    M = len(A[0])
    if M == 0:
        return 0
    # finish boundary case check

    countries = 0

    def dfs(A, i, j, c):
        """
        deep first search
        :param A: the matrix.
        :param i: row index i
        :param j: column index j
        :param c: original country c.
        :return: nothing.
        """
        if not (0 <= i < N) or not (0 <= j < M) or A[i][j] <= MIN:
            return
        if A[i][j] == c:  # same country.
            A[i][j] = MIN
            dfs(A, i - 1, j, c)
            dfs(A, i + 1, j, c)
            dfs(A, i, j - 1, c)
            dfs(A, i, j + 1, c)

    for i in range(N):
        for j in range(M):
            if A[i][j] <= MIN:  # already visited.
                continue
            countries += 1  # found a new country that has never been visited.
            dfs(A, i, j, A[i][j])  # go dfs to visit all the places of this
            # country.
    return countries
