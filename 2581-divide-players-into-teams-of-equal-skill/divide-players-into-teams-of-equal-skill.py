class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n%2 == 1:
            return -1
        totalTeams = n // 2
        total = sum(skill)
        if total % totalTeams != 0:
            return -1
        twoSum = total // totalTeams

        hashSet = defaultdict(int)

        ans = 0

        for num in skill:
            key = twoSum-num
            if hashSet[key] > 0:
                ans += num * key
                hashSet[key] -= 1
            else:
                hashSet[num] += 1
 
        if sum(hashSet.values()) != 0:
            return -1
        return ans
        