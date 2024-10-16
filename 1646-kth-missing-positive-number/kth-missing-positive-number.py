class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maxElement = max(arr)+k

        for i in range(1, maxElement+1):
            if i not in arr:
                k -= 1
            if k == 0:
                return i
        
            

        