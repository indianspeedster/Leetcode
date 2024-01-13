class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = Counter(s)
        t_count = Counter(t)
        more, less = 0, 0
        for key in t_count.keys():
            if key not in s_count.keys():
                more += t_count[key]
            else:
                if s_count[key]>t_count[key]:
                    less += s_count[key] - t_count[key]
                else:
                    more += t_count[key] - s_count[key] 

        return max(more, less)


        