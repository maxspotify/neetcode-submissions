class Solution:
    def climbStairs(self, n: int) -> int:
        # dp
        my_dict = {1: 1, 2: 2}

        def climb(n):
            if n in my_dict:
                return my_dict[n]
            val = climb(n-1) + climb(n-2)
            my_dict[n] = val
            return val
        
        return climb(n)
