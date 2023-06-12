class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start, end = nums[0], nums[0]
        ans = []
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1]==1:
                end = nums[i]
            else:
                if start==end:
                    ans.append(f"{start}")
                else:
                    ans.append(f"{start}->{end}")
                start , end = nums[i], nums[i]
        if start==end:
            ans.append(f"{start}")
        else:
            ans.append(f"{start}->{end}")
        return ans
        
        