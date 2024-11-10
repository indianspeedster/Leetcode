class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        hashMap = {i:0 for i in range(32)}
        def seti(x):
            for i in range(32):
                bit = x >> i & 1
                hashMap[i] += bit
        def unset(x):
            for i in range(32):
                bit = x>>i & 1
                hashMap[i] -= bit
        
        def numb():
            ans = 0
            for i in range(32):
                if hashMap[i] > 0:
                    ans += 2**i
            return ans
        left = 0
        ans = 10**9
        cur = 0
        for i, num in enumerate(nums):
            seti(num)
            cur = numb()
            while cur >= k and left <= i:
                ans = min(ans, i-left+1)
                unset(nums[left])
                left += 1
                cur = numb()
        return ans if ans != 10**9 else -1
            






            
        