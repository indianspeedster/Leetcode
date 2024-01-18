class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = []
        last = -1
        for num in nums1:
            start, end = 0,len(nums2)-1
            if num == last:
                continue
            while start <= end:
                mid = (start+end)//2
                if nums2[mid] == num:
                    ans.append(num)
                    break
                if nums2[mid] > num:
                    end = mid-1
                else:
                    start = mid+1
            last = num
        return ans
            
            



        