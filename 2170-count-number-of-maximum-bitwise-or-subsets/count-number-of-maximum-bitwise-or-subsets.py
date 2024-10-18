class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        hashMap = defaultdict(int)
        def dfs(ind, val):
            if ind == len(nums):
                hashMap[val] += 1
                return
            dfs(ind+1, val | nums[ind])
            dfs(ind+1, val)
        dfs(0, 0)
        key = max(hashMap.keys())
        return hashMap[key]

        