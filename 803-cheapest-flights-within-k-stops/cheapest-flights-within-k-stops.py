class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distance = [float("inf") for i in range(n)]
        distance[src] = 0

        for loop in range(k+1):
            temp = distance.copy()

            for start, end, charge in flights:
                if distance[start] == float("inf"):
                    continue
                
                if distance[start] + charge < temp[end]:
                    temp[end] = distance[start] + charge
            distance = temp
        return -1 if distance[dst] == float("inf") else distance[dst]

        