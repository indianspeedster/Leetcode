class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,h = 0,len(nums)-1
        arr = nums
        ans = nums[0]
        while l<=h:
            mid = (l+h)//2
            if arr[mid]<= arr[h]:
                ans = min(ans,arr[mid])
                h = mid-1
            else:
                ans = min(ans,arr[l])
                l = mid+1
        return ans
        