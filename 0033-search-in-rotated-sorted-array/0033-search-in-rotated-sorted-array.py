class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0, len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif nums[l]<=nums[mid]:
                if target in range(nums[l],nums[mid]+1):
                    h = mid-1
                else:
                    l = mid + 1
            else:
                if target in range(nums[mid],nums[h]+1):
                    l = mid+1
                else:
                    h=mid-1
        return -1
                
        