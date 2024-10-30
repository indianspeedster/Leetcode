class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        def LIS(nums_arr):
            position_arr = [0] * n
            stack = []
            for i in range(n):
                if stack and stack[-1] >= nums_arr[i]:
                    pos = bisect_left(stack, nums_arr[i])
                    stack[pos] = nums_arr[i]
                    position_arr[i] = pos+1
                else:
                    stack.append(nums_arr[i])
                    position_arr[i] = len(stack)
            return position_arr
        
        left, right = LIS(nums), LIS(nums[::-1])[::-1]
        ans = float('inf')
        for i in range(n):
            if left[i] > 1 and right[i] > 1:
                ans = min(ans, n - (left[i] + right[i]-1))

        return ans
        