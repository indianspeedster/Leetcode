class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def dfs(n,k):
            if n == len(arr):
                return 0
            accept = True
            l = set()
            for ind, char in enumerate(arr[n]):
                if char in k or char in l:
                    accept =False
                    break
                else:
                    l.add(char)
                
            if accept:
                pick = len(arr[n]) + dfs(n+1, k + arr[n])
            else:
                pick = 0
            npick = dfs(n+1, k)
            return max(pick, npick)
        return dfs(0, "")

        