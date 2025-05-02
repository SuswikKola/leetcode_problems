# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        set_a = set()
        def traverse(root):
            if root==None:
                return False
            if k-root.val in set_a:
                return True
            set_a.add(root.val)
            return traverse(root.left) or traverse(root.right)
        return traverse(root)