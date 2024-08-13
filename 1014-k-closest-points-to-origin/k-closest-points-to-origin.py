class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        storeDistances = []
        for point in points:
            distance = (point[0]**2 + point[1]**2)**0.5
            storeDistances.append((distance, point))
        ans = []
        heapq.heapify(storeDistances)
        for pop in range(k):
            popped = heapq.heappop(storeDistances)
            ans.append(popped[1])
        return ans
        