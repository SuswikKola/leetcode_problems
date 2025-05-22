# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        set_a = set()
        def check(root):
            if root==None:
                return 
            set_a.add(root.val)
            check(root.left)
            check(root.right)
        check(root)
        print(set_a)
        return len(set_a)==1