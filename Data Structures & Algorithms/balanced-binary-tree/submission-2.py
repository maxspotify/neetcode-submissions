# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_dfs(root):
            if not root:
                return (True, 1)
            
            left = height_dfs(root.left)
            right = height_dfs(root.right)

            is_balanced = abs(left[1] - right[1]) <= 1

            return ((is_balanced and left[0] and right[0]), 1 + max(left[1], right[1]))

        return height_dfs(root)[0]