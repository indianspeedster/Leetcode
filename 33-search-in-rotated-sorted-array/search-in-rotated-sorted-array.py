class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[right]:
                if target in range(nums[mid], nums[right]+1):
                    left = mid+1
                else:
                    right = mid-1
            else:
                if target in range(nums[left], nums[mid]):
                    right = mid-1
                else:
                    left = mid +1
        return ans  

        