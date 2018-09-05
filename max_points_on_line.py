# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):

    def same_line(self, A, B, C):
        if A[0] == B[0] and A[1] == B[1] or A[0] == C[0] and A[1] == B[1] \
                or C[0] == B[0] and C[1] == B[1]:
            return True
        if A[0] == B[0]:
            return A[0] == C[0]
        if A[1] == B[1]:
            return A[1] == C[1]
        a = float(C[1] - A[1]) * (B[0] - A[0])
        b = float(B[1] - A[1]) * (C[0] - A[0])
        return a == b

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        p_list = [[point.x, point.y] for point in points]
        point2count = dict()
        for point in p_list:
            point2count[str(point)] = point2count.get(str(point), 0) + 1
        p_set = point2count.keys()
        
        if len(points) <= 2:
            return len(points)
        MAX = 2
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                A = points[i]
                B = points[j]

                count = point2count.get(str(A)) + point2count.get(str(B))
                print('=======================================================')
                print('point (%d,%d) and point (%d,%d) :' % (p_list[i][0],
                                                             p_list[i][1],
                                                             p_list[j][0],
                                                             p_list[j][1]))
                for k in range(j + 1, len(points)):
                    if self.same_line(p_list[i],
                                      p_list[j],
                                      p_list[k]):
                        count += point2count.get()
                MAX = max(MAX, count)
                print('=======================================================')

        return MAX


t_input = [[0, 9], [138, 429], [115, 359], [115, 359], [-30, -102], [230, 709],
           [-150, -686], [-135, -613], [-60, -248], [-161, -481], [207, 639],
           [23, 79],
           [-230, -691], [-115, -341], [92, 289], [60, 336], [-105, -467],
           [135, 701],
           [-90, -394], [-184, -551], [150, 774]]

s = Solution()
points = [Point(i[0], i[1]) for i in t_input]

print s.maxPoints(points)
