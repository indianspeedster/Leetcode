class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        last = -1
        for num in nums1:
            i,j = 0,len(nums2)-1
            if num == last:
                continue
            while i <= j:
                mid = (i+j)//2
                if nums2[mid] == num:
                    ans.append(num)
                    break
                if nums2[mid] > num:
                    j = mid-1
                else:
                    i = mid+1
            last = num
        return ans
            
            



        