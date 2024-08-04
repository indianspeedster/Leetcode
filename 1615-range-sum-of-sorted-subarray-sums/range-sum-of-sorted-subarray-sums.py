class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        lenNums = len(nums)
        for i in range(lenNums):
            subSum = 0
            for j in range(i, lenNums):
                subSum += nums[j]
                arr.append(subSum)
        arr.sort()
        
        return sum(arr[left-1:right]) % (10**9 +7)
        