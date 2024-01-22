class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hash_set = set()
        n = len(nums)
        repeated = -1
        for num in nums:
            if num in hash_set:
                repeated = num
                break
            else:
                hash_set.add(num)
        total = sum(nums)
        exact_total = n*(n+1)//2
        
        original = repeated + exact_total - total
        return [repeated, original]

        