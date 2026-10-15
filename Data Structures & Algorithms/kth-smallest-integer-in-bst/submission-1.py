# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        result = None
        def inorder_dfs_search(root):
            nonlocal result, k
            if not root:
                return
            
            inorder_dfs_search(root.left)
            if k == 1:
                result = root.val
                k -= 1
                return
            k -= 1
            inorder_dfs_search(root.right)
        
        inorder_dfs_search(root)
        
        return result

        