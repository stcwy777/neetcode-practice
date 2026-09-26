class ListNode:
    def __init__(self, val: int, next: ListNode = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self._len = 0
        self._head = None
        self._tail = None
    
    def get(self, index: int) -> int:
        if index >= self._len:
            return -1
        p = self._head

        for i in range(index):
            p = p.next
        return p.val

    def insertHead(self, val: int) -> None:
        p = ListNode(val)
        p.next = self._head
        self._head = p
        self._len += 1
        if self._len == 1:
            self._tail = self._head

    def insertTail(self, val: int) -> None:
        p = ListNode(val)
        if self._tail:
            self._tail.next = p
            self._tail = p
        else:
            self._tail = p
            self._head = p

        self._len += 1

    def remove(self, index: int) -> bool:
        if index >= self._len:
            return False
        elif index == 0:
            p = self._head
            self._head = self._head.next
            self._len -= 1
            if self._len == 0:
                self._tail = None
            
            del p
            return True
                    
        p = self._head
        for i in range(index - 1):
            p = p.next
        
        q = p.next
        p.next = q.next

        if self._tail == q:
            self._tail = p
        self._len -= 1
        del q        
        return True

    def getValues(self) -> List[int]:
        rslt = []
        p = self._head
        print(self._len)
        for i in range(self._len):
            rslt.append(p.val)
            p = p.next
        return rslt
        
