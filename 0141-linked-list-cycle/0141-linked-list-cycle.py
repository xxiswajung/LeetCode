# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cycle=set()
        while head:
            if head in cycle:
                print(cycle)
                return True
            else:
                cycle.add(head)
                head=head.next