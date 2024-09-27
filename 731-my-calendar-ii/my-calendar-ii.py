class MyCalendarTwo:

    def __init__(self):
        self.overlapping = []
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s,e in self.overlapping:
            if  not (start >= e or s >= end):
                return False
        for s,e in self.calendar:
            if  not (start >= e or s >= end):
                st = max(s, start)
                en = min(e, end)
                self.overlapping.append((st, en))
        self.calendar.append((start, end))
        return True

        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
