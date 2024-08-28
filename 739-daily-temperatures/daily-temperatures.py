class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        ans = [0]*n
        for ind, temp in enumerate(temperatures):
            while st and temperatures[st[-1]] < temp:
                prev = st.pop()
                ans[prev] = ind - prev
            st.append(ind)
        

        return ans



        