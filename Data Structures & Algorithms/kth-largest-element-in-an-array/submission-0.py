class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg = [-num for num in nums]
        heapq.heapify(neg)

        k -= 1
        while k:
            heapq.heappop(neg)
            k -= 1
        
        return -heapq.heappop(neg)