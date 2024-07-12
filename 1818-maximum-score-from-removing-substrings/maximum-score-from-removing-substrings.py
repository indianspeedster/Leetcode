class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        st = []
        if x > y:
            for i in s:
                if i == "b" and st and  st[-1] == "a":
                    ans += x
                    st.pop()
                    continue
                st.append(i)
            s = "".join(st)
            print(s)
            st = []
            for i in s:
                if i == "a" and st and st[-1] == "b":
                    ans += y
                    st.pop()
                    continue
                st.append(i)
        else:
            for i in s:
                if i == "a" and st and st[-1] == "b":
                    ans += y
                    st.pop()
                    continue
                st.append(i)
            s = "".join(st)
            st = []
            for i in s:
                if i == "b" and st and  st[-1] == "a":
                    ans += x
                    st.pop()
                    continue
                st.append(i)
        return ans

        



            
        