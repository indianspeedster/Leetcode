class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = []
        self.k = k
        
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr = [value] + self.arr
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr.append(value)
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False      
        self.arr = self.arr[1:]
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False      
        self.arr.pop()
        return True
        

    def getFront(self) -> int:
        return self.arr[0] if len(self.arr) > 0 else -1
        

    def getRear(self) -> int:
        return self.arr[-1] if len(self.arr) > 0 else -1
        

    def isEmpty(self) -> bool:
        return len(self.arr) == 0
        

    def isFull(self) -> bool:
        return len(self.arr) == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()