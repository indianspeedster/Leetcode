class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDic = Counter(nums)
        ans = []

        for key, value in sorted(countDic.items(), key = lambda x : x[1], reverse=True):
            ans.append(key)
            k -= 1
            if k == 0:
                return ans
        