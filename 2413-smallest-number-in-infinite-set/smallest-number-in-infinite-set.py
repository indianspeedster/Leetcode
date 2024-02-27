class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [i for i in range(1,1001)]
        self.set1 = set(self.arr)
        

    def popSmallest(self) -> int:
        popped = heapq.heappop(self.arr)
        self.set1.remove(popped)
        return popped
        

    def addBack(self, num: int) -> None:
        if num not in self.set1:
            self.set1.add(num)
            heapq.heappush(self.arr, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)