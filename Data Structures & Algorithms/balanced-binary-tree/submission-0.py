# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # brute force
        def dfs(root, height):
            if not root:
                return height
            left_height = dfs(root.left, height + 1)
            right_height = dfs(root.right, height + 1)
            return max(left_height, right_height)

        if not root:
            return True
        
        balanced = abs(dfs(root.left, 0) - dfs(root.right, 0)) <= 1
        return balanced and self.isBalanced(root.left) and self.isBalanced(root.right)
            
            

        