class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        countDict = Counter(arr)
        count = 0
        for string in arr:
            if countDict[string] == 1:
                count += 1
            if count == k:
                return string
        return ""
        
        