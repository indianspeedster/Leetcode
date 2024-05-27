class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            element = i + 1
            count = 0
            for num in nums:
                if num >= element:
                    count += 1
            if element  == count:
                return element
        return -1

        