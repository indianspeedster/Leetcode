class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        N = len(nums)
        Q = len(queries)

        events = defaultdict(list)

        for index, (s,e) in enumerate(queries):
            events[s].append((index, 1))
            events[e].append((index, -1))

        current = set()
        ans = [False]*Q

        for qi, t in events[0]:
            if t == 1:
                current.add(qi)
            else:
                if qi in current:
                    current.remove(qi)
                    ans[qi] = True
        

        for i in range(1, N):
            if nums[i] % 2 == nums[i-1] %2:
                current = set()

            for qi, t in events[i]:
                if t == 1:
                    current.add(qi)
                else:
                    if qi in current:
                        current.remove(qi)
                        ans[qi] = True
        return ans
        