class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        hash_map = defaultdict(int)
        for num in nums:
            if hash_map[k-num] > 0:
                hash_map[k-num] -= 1
                ans += 1
            else:
                hash_map[num] += 1
        return ans
        