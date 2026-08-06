# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k == 1:
            return head

        tail = None
        start = head
        end = head
        count = 0
        while end:
            end = end.next
            count += 1

            if count % k == 0:
                # reverse from start to node
                pre, cur, nxt = end, start, None
                # print(count, cur.val)
                while cur != end:
                    nxt = cur.next
                    cur.next = pre
                    pre = cur
                    cur = nxt

                if count == k:
                    head = pre
                else:
                    # print(tail.val, pre.val)
                    tail.next = pre
                tail = start
                start = cur

        return head