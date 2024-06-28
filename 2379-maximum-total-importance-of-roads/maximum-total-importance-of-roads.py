class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(int)
        for start, end in roads:
            dic[start] += 1
            dic[end] += 1
        val1 = n
        dic2 = defaultdict(int)
        for key, val in sorted(dic.items(), key = lambda x : x[1], reverse=True):
            dic2[key] = val1
            val1 -= 1
        ans = 0
        for start, ends in roads:
            ans += dic2[start] + dic2[ends]
        print(dic2)
        return ans
            
        