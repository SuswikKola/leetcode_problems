# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def insert(root,val):
            if root==None:
                return TreeNode(val)
            if root.val<val:
                root.right = insert(root.right,val)
            else:
                root.left = insert(root.left,val)
            return root
        res = []
        def trim(root):
            if root==None:
                return
            if root.val>=low and root.val<=high:
                res.append(root.val)
            trim(root.left)
            trim(root.right)
        trim(root)
        root= None
        for i in res:
            root = insert(root,i)
        return root
            