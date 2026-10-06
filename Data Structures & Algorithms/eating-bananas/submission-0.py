import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            result = 0
            for pile in piles:
                result += math.ceil(pile/k)
            return result <= h


        low = 1
        high = max(piles)
        result = high

        while low <= high:
            k = (low + high) // 2

            can_finish = canFinish(k)

            if can_finish:
                result = k
                high = k - 1
            else:
                low = k + 1

        return result

