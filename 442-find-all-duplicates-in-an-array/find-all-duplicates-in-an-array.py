class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mapper = set()
        ans = []
        for num in nums:
            if num in mapper:
                ans.append(num)
            else:
                mapper.add(num)
        return ans
        