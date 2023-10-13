# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        cnt=1
        while head.next!=None:
            head=head.next
            cnt+=1
        v=cnt//2+1
        cnt2=1
        while cnt2!=v:
            cur=cur.next
            cnt2+=1
        return cur