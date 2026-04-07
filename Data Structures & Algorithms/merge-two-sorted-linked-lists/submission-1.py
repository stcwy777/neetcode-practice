# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # head = None

        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        # if list1.val <= list2.val:
        #     head = list1
        #     trav1 = list1.next
        # else:
        #     head = list2
        #     trav2 = list2.next
        
        dummy = ListNode(0)
        trav3 = dummy
        trav1 = list1
        trav2 = list2        
        while trav1 is not None and trav2 is not None:
            if trav1.val <= trav2.val:
                nxt_node = trav1
                trav1 = trav1.next
            else:
                nxt_node = trav2
                trav2 = trav2.next
            
            trav3.next = nxt_node
            trav3 = nxt_node
        
        if trav1 is not None:
            trav3.next = trav1
        else:
            trav3.next = trav2
        return dummy.next
        