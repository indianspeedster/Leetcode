class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0
        arr = []
        for char in s[::-1]:
            arr.append(a_count)
            if char == "a":
                a_count += 1
        b_count = 0
        arr = arr[::-1]
        ans = len(s)
        for i, j in enumerate(s):
            ans = min(ans, b_count + arr[i])
            if j == "b":
                b_count += 1
        return ans

        