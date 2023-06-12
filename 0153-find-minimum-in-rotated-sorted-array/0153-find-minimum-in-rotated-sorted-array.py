class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        ans = float("inf")
        while low<=high:
            mid = (low+high)>>1
            if nums[low]> nums[mid]:
                ans = min(nums[mid], ans)
                high = mid - 1
            else:
                ans = min(nums[low], ans)
                low = mid + 1

        return ans
                
                
        