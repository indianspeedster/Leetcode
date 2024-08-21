class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        ans = []
        heapq.heapify(nums)
        while nums:
            ans.append(heapq.heappop(nums))
        return ans