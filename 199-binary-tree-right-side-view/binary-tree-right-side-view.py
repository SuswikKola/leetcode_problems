# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dict_a = {}
        def rightView(root,d):
            if root==None:
                return 
            if d not in dict_a:
                dict_a[d]=root.val
            else:
                dict_a[d]=root.val
            rightView(root.left,d+1)
            rightView(root.right,d+1)
        rightView(root,0)
        res = []
        for i in dict_a:
            res.append(dict_a[i])
        return res
