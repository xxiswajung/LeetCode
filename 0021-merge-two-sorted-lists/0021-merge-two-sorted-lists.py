# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode() #헤더(맨 앞) 선언해서 연결리스트 생성
        cur = node #얘로 연결리스트를 끝까지 만들예정
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        #cur 의 역할 : node가 해야 할 일(=다른 노드 잇는 일)을 대신해주되, 맨 앞으로 못 가기 때문에 전체 리스트를 출력X
        #node의 역할 : 따라서 맨 앞자리를 지키고 있는 node를 남겨두고, cur로 복사해야함
        return node.next
            

                    