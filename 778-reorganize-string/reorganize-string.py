class Solution:
    def reorganizeString(self, s: str) -> str:
        stringCounter = Counter(s)
        n = math.ceil(len(s)/2)
        for count in stringCounter.values():
            if count > ( n ):
                return ""
        k = []
        ans = "*"
        for key, val in stringCounter.items():
            k.append([-1*val, key])
        heapq.heapify(k)
        while k:
            element = heapq.heappop(k)
            if ans[-1] != element[1]:
                ans += element[1]
                element[0] += 1
                if element[0] < 0:
                    heapq.heappush(k, element)
            else:
                element2 = heapq.heappop(k)
                ans += element2[1]
                element2[0] += 1
                if element2[0]<0:
                    heapq.heappush(k, element2)
                heapq.heappush(k, element)
        return ans[1:]