import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x1, y1, x2=0, y2=0):
            return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

        points = [(distance(x, y), [x, y]) for x, y in points]
        heapq.heapify(points)

        result = []
        for i in range(k):
            val = heapq.heappop(points)
            result.append(val[1])
        return result