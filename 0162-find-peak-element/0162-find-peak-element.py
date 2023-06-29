class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [float("-inf")] + nums + [float("-inf")]
        for i in range(1,n+1):
            if arr[i]> arr[i-1] and arr[i]> arr[i+1]:
                return i-1
        
        