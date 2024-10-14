class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-1*num for num in nums]
        heapq.heapify(nums)
        ans = 0

        for op in range(k):
            val = -1 * heapq.heappop(nums)

            ans += val
            val = ceil(val / 3)
            heapq.heappush(nums, -1*val)
        return ans
        