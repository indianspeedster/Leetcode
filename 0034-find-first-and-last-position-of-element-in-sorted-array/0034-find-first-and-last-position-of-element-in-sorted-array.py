class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower():
            l,h = 0,len(nums)-1
            ans = -1
            while l<=h:
                mid = (l+h)//2
                print(mid)
                if nums[mid]==target:
                    h = mid-1
                    ans = mid
                elif nums[mid]>target:
                    h = mid-1
                else:
                    l = mid+1
            return ans
        def higher():
            l,h = 0,len(nums)-1
            ans = -1
            while l<=h:
                mid = (l+h)//2
                if nums[mid]==target:
                    l = mid+1
                    ans = mid
                elif nums[mid]>target:
                    h = mid-1
                else:
                    l = mid+1
            return ans
        return [lower(),higher()]