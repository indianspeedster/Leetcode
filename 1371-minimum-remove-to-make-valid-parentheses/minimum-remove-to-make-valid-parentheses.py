class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = []
        st = []
        for i in s:
            if st:
                if i == ")":
                    st.pop()
                    ans.append(i)
                elif i =="(":
                    st.append(i)
                    ans.append(i)
                else:
                    ans.append(i)
            else:
                if i == ")":
                    continue
                elif i == "(":
                    st.append(i)
                    ans.append(i)
                else:
                    ans.append(i)
        print(st)
        k = len(st)
        ansk = ""
        for i in ans[::-1]:
            if i == "(" and k != 0:
                k -= 1
                continue
            else:
                ansk += i
        return ansk[::-1]

        