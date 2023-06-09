class Solution:
    def findMin(self, nums: List[int]) -> int:
        arr = nums
        l,h = 0, len(arr)-1
        ans =nums[0]
        while l<=h:
            mid = (l+h)//2
            if arr[mid]==arr[l]==arr[h]:
                ans = min(ans,arr[mid])
                l = l+1
                h = h-1
            elif arr[l]<= arr[mid]:
                ans = min(ans, arr[l])
                l = mid+1
            else:
                ans = min(ans, arr[mid])
                h = mid - 1
        return ans