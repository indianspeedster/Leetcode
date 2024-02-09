class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        numLength = len(nums)
        nums.sort()
        dp = [1]*numLength
        temp = [i for i in range(numLength)]
        maxi = 1
        cur = 0
        for i in range(numLength):
            for j in range(i):
                if nums[i]%nums[j] == 0 and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
                    temp[i] = j
            if dp[i] > maxi:
                maxi = dp[i]
                cur = i
        ans = [nums[cur]]

        while cur!=temp[cur]:
            cur = temp[cur]
            ans.append(nums[cur])
        return ans

                