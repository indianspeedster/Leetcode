class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        left = 0
        ans = []
        n = len(nums)
        consec = 1
        for i in range(n):
            if i > 0 and nums[i] == 1 + nums[i-1]:
                consec += 1
            if i-left + 1 > k:
                if nums[left] + 1 == nums[left+1]:
                    consec -= 1
                left += 1
            
            if i - left + 1 == k:
                if consec == k:
                    ans.append(nums[i])
                else:
                    ans.append(-1)
        return ans
            


        


        