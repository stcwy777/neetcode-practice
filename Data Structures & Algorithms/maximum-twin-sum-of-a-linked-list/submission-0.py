# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node = head
        
        store = []
        while node:
            store.append(node.val)
            node = node.next
        
        sumMax = 0

        for i in range(len(store) // 2):
            sumMax = max(sumMax, store[i] + store[len(store) - 1 - i])
        
        return sumMax
