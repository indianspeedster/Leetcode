class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = []
        right= []
        total = 0
        stack = []
        for i, num in enumerate(arr):
            pi = i
            while len(stack)>0 and stack[-1][1]>=num:
                pi, _ = stack.pop()
            stack.append((pi, num))
            left.append(i - pi + 1)
        stack = []
        for i, num in enumerate(reversed(arr)):
            pi = i
            while len(stack)>0 and stack[-1][1]>num:
                pi, _ = stack.pop()
            stack.append((pi, num))
            right.append(i - pi + 1)
        right.reverse()
        for i, num in enumerate(arr):
            total += num *left[i]*right[i]
        
        return total % (10**9 + 7)
            

        