class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        countdic = defaultdict(int)
        count = 0
        for i in range(len(arr)-1):
            xori = 0
            for j in range(i+1, len(arr)):
                xori ^= arr[j-1]
                xorj = 0
                for k in range(j, len(arr)):
                    xorj ^= arr[k]
                    if xori == xorj:
                        count += 1

        
        return count
        