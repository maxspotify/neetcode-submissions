class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i, v in enumerate(nums):
            if target - v in diffs:
                return [diffs[target-v], i]
            diffs[v] = i
        