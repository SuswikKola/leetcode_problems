# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = ListNode(0)
        dum1 = temp1
        temp2 = ListNode(0)
        dum2 = temp2
        temp = head
        ind = 0
        while temp:
            if ind%2==0:
                temp1.next = ListNode(temp.val)
                temp1 = temp1.next
                ind+=1
            else:
                temp2.next = ListNode(temp.val)
                temp2 = temp2.next
                ind+=1
            temp=temp.next
        temp1.next = dum2.next
        return dum1.next
        