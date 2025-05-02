# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l = [0]*101
        cur = root
        def traverse(cur):
            if cur==None:
                return
            l[cur.val]=cur.val
            traverse(cur.left)
            traverse(cur.right)
        traverse(cur)
        cur2 = root
        def change(cur2):
            if cur2==None:
                return
            cur2.val = sum(l[cur2.val:])
            change(cur2.left)
            change(cur2.right)
        change(cur2)
        return root