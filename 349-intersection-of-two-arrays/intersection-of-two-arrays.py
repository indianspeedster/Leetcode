class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = [-1]
        i,j = 0,0
        while i <= len(nums1)-1 and j <= len(nums2)-1:
            if nums1[i] == nums2[j]:
                if ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return ans[1:]
            
            



        