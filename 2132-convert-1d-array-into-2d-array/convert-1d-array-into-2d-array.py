class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(original): return []

        ans = []
        prev = 0
        for i in range(1,m+1):
            ans.append(original[prev:i*n])
            prev = i*n 
        return ans      