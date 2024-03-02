class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        ans = []
        for num in nums:
            if num >= 0:
                pos.append(num**2)
            else:
                neg.append(num**2)
        neg = neg[::-1]
        i,j = 0,0
        while i < len(pos) and j < len(neg):
            if pos[i] <= neg[j]:
                ans.append(pos[i])
                i += 1
            else:
                ans.append(neg[j])
                j += 1
        if i < len(pos):
            ans.extend(pos[i:])
        if j < len(neg):
            ans.extend(neg[j:])
        return ans
        