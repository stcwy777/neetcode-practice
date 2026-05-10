class SegmentTree:
    def __init__(self, L: int, R: int):
        self.L = L
        self.R = R
        self.left = None
        self.right = None

    def query(self, L: int, R: int) -> bool:
        if R <= self.L:
            if self.left is None:
                self.left = SegmentTree(L, R)
                return True
            else:
                return self.left.query(L, R)
        elif L >= self.R:
            if self.right is None:
                self.right = SegmentTree(L, R)
                return True
            else:
                return self.right.query(L, R)
        else:
            print(L, R, self.L, self.R)
            return False

class MyCalendar:
    
    def __init__(self):
        self.calendar = None

    def book(self, startTime: int, endTime: int) -> bool:
        if self.calendar is None:
            self.calendar = SegmentTree(startTime, endTime)
            return True
        else:
            return self.calendar.query(startTime, endTime)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)