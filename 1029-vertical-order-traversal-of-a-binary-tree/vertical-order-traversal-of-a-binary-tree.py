from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict_a = defaultdict(list)

        def check(node, row, col):
            if not node:
                return
            dict_a[col].append((row, node.val))
            check(node.left, row + 1, col - 1)
            check(node.right, row + 1, col + 1)

        check(root, 0, 0)

        res = []
        for col in sorted(dict_a.keys()):
            sorted_nodes = sorted(dict_a[col], key=lambda x: (x[0], x[1]))
            res.append([val for row, val in sorted_nodes])
        return res
