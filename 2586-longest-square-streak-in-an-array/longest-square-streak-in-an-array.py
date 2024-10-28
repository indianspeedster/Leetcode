class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse = True)

        counter = defaultdict(int)
        ans = -1

        for x in nums:
            if x*x in counter:
                counter[x] = 1 + counter[x*x]
            else:
                counter[x] = 1
            if counter[x] > 1:
                ans = max(ans, counter[x])
        return ans

        
        