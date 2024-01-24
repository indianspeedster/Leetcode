class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = max(nums)
        nums_set = set(nums)
        for i in range(1, length):
            if i not in nums_set:
                return i
        if length +1 <= 0:
            return 1
        return length + 1


        