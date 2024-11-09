class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        countNum = Counter(nums)

        nums.sort()

        def maxFreq(x):
            count = countNum[x]
            left = bisect.bisect_left(nums, x-k)
            right = bisect.bisect_right(nums, x+k)

            totalCount = min (right-left-count, numOperations)

            return totalCount + count
        
        ans = 0

        for i in range(nums[0], nums[-1]+1):

            ans = max(ans, maxFreq(i))

        return ans

            

        