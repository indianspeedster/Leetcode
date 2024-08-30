class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [(-1*val,key) for key, val in count.items()]
        heapq.heapify(arr)
        ans = []
        for i in range(k):
            val, key = heapq.heappop(arr)
            ans.append(key)
        return ans