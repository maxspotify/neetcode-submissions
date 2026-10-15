# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {v: i for i, v in enumerate(inorder)}

        def helper(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            
            root = TreeNode(preorder[preorder_left])

            mid = index_map[preorder[preorder_left]]
            left_start_inorder = inorder_left
            left_end_inorder = mid - 1
            right_start_inorder = mid + 1
            right_end_inorder = inorder_right

            left_start_preorder = preorder_left + 1
            left_end_preorder = left_start_preorder + left_end_inorder - left_start_inorder
            right_start_preorder = left_end_preorder + 1
            right_end_preorder = preorder_right

            root.left = helper(left_start_preorder, left_end_preorder, left_start_inorder, left_end_inorder)
            root.right = helper(right_start_preorder, right_end_preorder, right_start_inorder, right_end_inorder)
            return root
        
        return helper(0, len(preorder)-1, 0, len(inorder)-1)