class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums
            n = len(nums)
            l1 = mergeSort(nums[:n//2])
            l2 = mergeSort(nums[n//2:])
            return merge(l1, l2)
        def merge(l1, l2):
            ans = []
            i, j = 0, 0
            while i < len(l1) and j < len(l2):
                if l1[i] > l2[j]:
                    ans.append(l1[i])
                    i += 1
                else:
                    
                    ans.append(l2[j])
                    j += 1
            while i < len(l1):
                ans.append(l1[i])
                i += 1
            while j < len(l2):
                ans.append(l2[j])
                j += 1
            return ans
        return mergeSort(nums)[::-1]
            
        