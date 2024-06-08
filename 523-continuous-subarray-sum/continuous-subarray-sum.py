class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        lookup = set()
        q = deque()
        q.append(0)
        current = 0

        for i in range(len(nums)):
            current += nums[i]
            current %= k
            q.append(current)
            if current in lookup:
                return True
            
            if len(q)>1:
                lookup.add(q.popleft())
        return False
        