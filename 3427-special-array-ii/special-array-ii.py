class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        N = len(nums)

        track = [1]*N

        for i in range(1, N):
            if nums[i]%2 != nums[i-1]%2:
                track[i] = 1 + track[i-1]
        ans = []

        for start, end in queries:
            if end - start +1 <= track[end]:
                ans.append(True)
            else:
                ans.append(False)
        return ans