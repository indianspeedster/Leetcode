class Solution:
    def maxUniqueSplit(self, s: str) -> int:


        def dfs(i, cur_set):
            if i == len(s):
                return 0
            
            res = 0

            for j in range(i, len(s)):
                cur_str = s[i:j+1]
                if cur_str in cur_set:
                    continue
                cur_set.add(cur_str)
                res = max(res, 1+dfs(j+1, cur_set))
                cur_set.remove(cur_str)
            return res
        
        return dfs(0, set())
            

        