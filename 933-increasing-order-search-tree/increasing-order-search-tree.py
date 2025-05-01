# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def insert(root,val):
            if root==None:
                return TreeNode(val)
            root.right = insert(root.right,val)
            return root
        
        l = []
        def traversal(root):
            if root==None:
                return
            l.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        l.sort()
        root = None
        for i in l:
            root = insert(root,i)
        return root
        
