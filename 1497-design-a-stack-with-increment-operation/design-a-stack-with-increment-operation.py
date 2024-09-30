class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
        

    def pop(self) -> int:
        if not self.stack:
            return -1
        ele = self.stack.pop()
        return ele
        

    def increment(self, k: int, val: int) -> None:
        print(self.stack)
        length = len(self.stack)
        if k >= length:
            for i in range(length):
                self.stack[i] += val
        else:
            for i in range(k):
                self.stack[i] += val
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)