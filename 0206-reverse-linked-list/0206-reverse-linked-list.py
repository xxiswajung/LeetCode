# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new=None
        cur=head
        
        while cur:
            next_n=cur.next #cur의 다음 노드를 지시하는 next를 한 칸 전진
            cur.next=new #reverse
            new=cur #cur의 전 노드를 지시하는 new를 한 칸 전진, new: 2->1
            cur=next_n #cur 한칸 전진
        return new
