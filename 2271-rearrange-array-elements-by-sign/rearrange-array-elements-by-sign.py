class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []
        ans = []
        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)
        for i, num in enumerate(pos):
            ans.append(num)
            ans.append(neg[i])
        return ans
        