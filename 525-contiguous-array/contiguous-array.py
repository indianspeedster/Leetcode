class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero, ones = 0,0
        hashMap = {}
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                zero += 1
            else:
                ones += 1
            if ones - zero not in hashMap:
                hashMap[ones-zero] = i
            if ones == zero:
                res = i+1
            else:
                res = max(res,i - hashMap[ones-zero])
        return res
        

        