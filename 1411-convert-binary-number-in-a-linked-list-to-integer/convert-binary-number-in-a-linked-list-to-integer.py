# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s =""
        temp = head
        while temp:
            s+=str(temp.val)
            temp= temp.next
        res = 0
        track = 1
        j=0
        for i in s[::-1]:
            if i=="1":
                res+=(2**j)
            j+=1
        return (res)