class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        countVal = Counter(nums)
        ans = []
        for key, val in sorted(countVal.items(), key = lambda x: (x[1], -x[0])):
            ans += [key] * val
        return ans
        