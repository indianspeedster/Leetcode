class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        countdic = defaultdict(int)
        count = 0
        for i in range(len(arr)-1):
            xori = arr[i]
            for j in range(i+1, len(arr)):
                xori ^= arr[j]
                if xori == 0:
                    count += j-i
                
        
        return count
        