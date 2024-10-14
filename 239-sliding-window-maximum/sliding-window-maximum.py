class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
            return nums
        
        res = []
        queue = collections.deque([])
        for i in range(k):
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])
        for i in range(k,len(nums)):
            if i-k == queue[0]:
                queue.popleft()
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        return res

        