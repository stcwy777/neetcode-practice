# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        if k == 0 or (k == 1 and lists[0] is None):
            return None
        
        sentinel = ListNode()
        p = sentinel
        
        while True:
            move_next = None
            min = 1001
            for j in range(k):
                if lists[j] is not None:
                    if min > lists[j].val:
                        min = lists[j].val
                        move_next = j
            if move_next is None:
                break
            else:
                lists[move_next] = lists[move_next].next
                p.next = ListNode(min)
                p = p.next
        return sentinel.next