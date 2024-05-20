class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def dfs(i, arr):
            if i == len(nums):
                subsets.append(arr)
                return 
            dfs(i+1, arr + [nums[i]])
            dfs(i+1, arr)
            return
        

            return arr
        dfs(0, [])
        ans = 0
        for ele in subsets:
            xor = 0
            for num in ele:
                xor ^= num
            ans += xor
        return ans
