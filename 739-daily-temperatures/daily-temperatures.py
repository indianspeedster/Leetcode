class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []

        for ind, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                prev_day = stack.pop()
                ans[prev_day] = ind - prev_day 
            stack.append(ind)
        
        return ans
        