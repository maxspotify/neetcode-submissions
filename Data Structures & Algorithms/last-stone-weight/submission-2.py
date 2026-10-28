class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop(stones)
            stone_2 = heapq.heappop(stones)
            remaining_stone = stone_1 - stone_2
            heapq.heappush(stones, remaining_stone)
        if not stones:
            return 0
        return -stones[0]