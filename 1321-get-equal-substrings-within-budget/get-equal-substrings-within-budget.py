class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        arr = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        ans = 0
        start = 0
        curr = 0
        cost = maxCost
        while curr in range(len(arr)) :
            while curr in range(len(arr)) and arr[curr] > maxCost:
                curr += 1
                start = curr
                cost = maxCost
            if curr in range(len(arr)):
                cost -= arr[curr]
                if cost >= 0:
                    ans = max(curr-start+1, ans)
                else:
                    while cost < 0 and start < curr:
                        cost += arr[start]
                        start += 1
                    ans = max(curr-start+1, ans)
                curr += 1
        return ans

                     



        