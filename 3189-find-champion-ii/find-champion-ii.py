class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inDegree = [0]*n

        for node1, node2 in edges:
            inDegree[node2] += 1

        ans = -1

        for i , val in enumerate(inDegree):
            if val == 0 and ans == -1:
                ans = i
                continue
            if val == 0 and ans != -1:
                return -1
        return ans
        