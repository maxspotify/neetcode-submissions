# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMin(self, root):
        while root.left:
            root = root.left
        return root
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None # not found
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # begin deletion
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            min_of_right = self.findMin(root.right)
            root.val = min_of_right.val
            root.right = self.deleteNode(root.right, min_of_right.val)
        return root
        
