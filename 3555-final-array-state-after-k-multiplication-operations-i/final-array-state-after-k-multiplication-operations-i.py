class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = [(val, i) for i, val in enumerate(nums)]

        ans = [0]*len(nums)

        heapq.heapify(arr)

        for i in range(k):
            val , index = heapq.heappop(arr)
            val = multiplier * val

            heapq.heappush(arr, (val, index))
        
        for val , index in arr:
            ans[index] = val
        
        return ans
        