# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()

        result = []

        if root:
            queue.append(root)
        
        while queue:
            element_count = len(queue)
            while element_count > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if element_count == 1:
                    result.append(node.val)
                element_count -= 1

        return result
                