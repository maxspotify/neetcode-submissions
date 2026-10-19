class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def subs(arr, index):
            if index > (len(nums) - 1):
                result.append(arr)
                return
            
            subs(arr+[nums[index]], index + 1)
            subs(arr, index + 1)
        
        subs([], 0)
        return result
            