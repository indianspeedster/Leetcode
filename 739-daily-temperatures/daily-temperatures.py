class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = []
        st = []
        for i in range(n-1, -1, -1):
            if not st:
                st.append(i)
                ans.append(0)
                continue
            else:
                while st and temperatures[st[-1]] <= temperatures[i]:
                    st.pop()
                if st:
                    ans.append(st[-1]-i)
                else:
                    ans.append(0)
                st.append(i)
        return ans[::-1]