class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        t = 0
        for num in nums:
            t ^= num
        t ^= k
        r = 0
        while t > 0:
            r = r + t % 2
            t //= 2
        return r
        