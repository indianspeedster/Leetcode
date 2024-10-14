class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = Counter(nums)
        elements = [(-1*j,i) for i,j in countDict.items()]
        ans = []
        heapq.heapify(elements)
        for i in range(k):
            count,key = heapq.heappop(elements)
            ans.append(key)
        return ans
        
        
        
        