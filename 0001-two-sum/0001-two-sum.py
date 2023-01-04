class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}
        for i in range(len(nums)):
            if nums[i] not in mapper.keys():
                mapper[target-nums[i]] = i
            else:
                return [i,mapper[nums[i]]]