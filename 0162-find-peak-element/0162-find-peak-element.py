class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [float("-inf")] + nums + [float("-inf")]
        l,r = 1, len(arr)-2
        while l<=r:
            mid = (l+r)//2
            if arr[mid] > arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid -1
            if arr[mid]>arr[mid-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        
        