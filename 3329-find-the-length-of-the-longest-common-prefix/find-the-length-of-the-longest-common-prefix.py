class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hashSet = set()
        for num in arr2:
            hashSet.add(num)
            while num != 0:
                hashSet.add(num)
                num = num // 10
                
        ans = 0
        for num in arr1:
            while num != 0:
                if num in hashSet:
                    ans = max(ans, len(str(num)))
                    break
                num = num // 10

        return ans

        