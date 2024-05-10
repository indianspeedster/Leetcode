class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        nums = []
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                val = arr[i]/arr[j]
                heapq.heappush(nums, (val, (arr[i], arr[j])))
        for i in range(k-1):
            heapq.heappop(nums)
        _, ans = heapq.heappop(nums)
        return list(ans)
        