class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(t[0], t[1], i) for i, t in enumerate(times)]
        times.sort()
        usedChairs = []
        availableChairs = [i for i in range(len(times))]

        for s,l,i in times:
            while usedChairs and usedChairs[0][0] <= s:
                lu,chair = heapq.heappop(usedChairs)
                heapq.heappush(availableChairs, chair)
            chair = heapq.heappop(availableChairs)
            heapq.heappush(usedChairs, (l, chair))
            if i == targetFriend:
                return chair 


        