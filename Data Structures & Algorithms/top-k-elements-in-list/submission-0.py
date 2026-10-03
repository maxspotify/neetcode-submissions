import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        
        heap = [(-val, num) for num, val in my_dict.items()]
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result