class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for ind, num in enumerate(nums):
            req = target-num
            if req in dic:
                return [dic[req], ind]
            else:
                dic[num] = ind
        