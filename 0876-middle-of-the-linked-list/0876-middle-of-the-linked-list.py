# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt=0
        node=head
        while node:
            cnt+=1
            node=node.next
        cnt=cnt//2
        while cnt!=0:
            cnt-=1
            head=head.next
        return head