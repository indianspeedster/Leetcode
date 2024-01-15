class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        team_dict = {}
        for winner, loser in matches:
            if winner not in team_dict:
                team_dict[winner] = [0,0]
            if loser not in team_dict:
                team_dict[loser] = [0,0]
            team_dict[winner][1] += 1
            team_dict[loser][0] += 1
        ans = [[],[]]
        
      
        for key,value in team_dict.items():
            if value[0] == 0:
                ans[0].append(key)
            if value[0] == 1:
                ans[1].append(key)

        return [sorted(i) for i in ans]
        