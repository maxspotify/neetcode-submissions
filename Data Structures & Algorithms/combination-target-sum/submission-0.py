class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        curr = []

        def backtrack(i, inc):
            if i > len(nums) - 1:
                return
            if inc > target:
                return
            if inc == target:
                result.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i, inc + nums[i])

            curr.pop()
            backtrack(i+1, inc)
        
        backtrack(0, 0)
        return result
            