# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dict_a = {}
        for i in nums:
            if i not in dict_a:
                dict_a[i]=1
            else:
                dict_a[i]+=1
        res = ListNode(0)
        temp = res

        while head:
            if head.val not in dict_a:
                temp.next = ListNode(head.val)
                temp=temp.next
            head=head.next
        return res.next

