class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        start = 0

        ans = []

        for i, val in enumerate(s):
            
            if start < len(spaces) and  i == spaces[start]:
                start += 1
                ans += " "
            ans.append(val)
        return "".join(ans)
        