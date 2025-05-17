# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if not head:
            return []
        l = []
        while head:
            l.append(head.val)
            head = head.next

        n = len(l)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and l[i] > l[stack[-1]]:
                j = stack.pop()
                result[j] = l[i]
            stack.append(i)

        return result