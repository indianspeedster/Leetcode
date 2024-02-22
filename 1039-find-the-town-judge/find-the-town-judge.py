class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trust_dict = {}
        for tr, tre in trust:
            if tr not in trust_dict:
                trust_dict[tr] = [0,0]
            if tre not in trust_dict:
                trust_dict[tre] = [0,0]
            trust_dict[tr][0] += 1
            trust_dict[tre][1] += 1
        for people in trust_dict:
            if trust_dict[people][0] == 0 and trust_dict[people][1] == n-1:
                return people
        return -1 
        