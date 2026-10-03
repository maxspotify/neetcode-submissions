class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3
        for num in nums:
            buckets[num] += 1
        
        nums_idx = 0
        for i, v in enumerate(buckets):
            while v:
                nums[nums_idx] = i
                v -= 1
                nums_idx += 1
            
        return nums
            




        