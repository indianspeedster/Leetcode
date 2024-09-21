class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = [str(i) for i in range(1, n+1)]
        return [int(i) for i in sorted(arr)]
        