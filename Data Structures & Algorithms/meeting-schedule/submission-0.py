"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = []

        for interval in intervals:
            start, end = interval.start, interval.end

            if not meetings:
                meetings.append((start, end))
                continue
            
            for s, e in meetings:

                if not ((end <= s) or (start >= e)):
                    return False
            
            meetings.append((start, end))
        
        return True