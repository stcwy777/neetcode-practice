# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2

        head = ListNode()
        n3 = head
        res = 0
        while n1 and n2:
            n3.next = ListNode((n1.val + n2.val + res) % 10)
            res = (n1.val + n2.val + res) // 10
            n3 = n3.next
            n1 = n1.next
            n2 = n2.next
        
        l = n1 if n1 else n2

        while l:
            n3.next = ListNode((l.val + res) % 10)
            res = (l.val + res) // 10
            l = l.next
            n3 = n3.next
        
        if res:
            n3.next = ListNode(res)

        return head.next
            