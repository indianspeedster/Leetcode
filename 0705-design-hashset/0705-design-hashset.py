class MyHashSet:

    def __init__(self):
        self.hash = []
        

    def add(self, key: int) -> None:
        if key not in self.hash:
            self.hash.append(key)
        

    def remove(self, key: int) -> None:
        for i in range(len(self.hash)):
            if key == self.hash[i]:
                self.hash.pop(i)
                break
        

    def contains(self, key: int) -> bool:
        for i in self.hash:
            if key == i:
                return True
        return False
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)