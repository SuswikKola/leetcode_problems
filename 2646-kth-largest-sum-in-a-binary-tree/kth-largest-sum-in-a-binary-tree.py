# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def level(root):
            dict_a = {}
            def check(root,d):
                if root==None:
                    return
                if d not in dict_a:
                    dict_a[d]=0
                dict_a[d]+=root.val
                check(root.left,d+1)
                check(root.right,d+1)
            check(root,0)
            return dict_a
        check = level(root)
        res = dict(sorted(check.items(),key=lambda x:x[1],reverse=True))
        print(res)
        if len(res)>=k:
            for i in res:
                if k==1:
                    return res[i]
                k-=1
        return -1
