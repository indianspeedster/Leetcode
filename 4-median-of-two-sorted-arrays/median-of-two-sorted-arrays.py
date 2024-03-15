class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        medianCount = len(nums1) + len(nums2)
        keepTrack =  medianCount // 2  - 1
        keepTrack = max(0, keepTrack)
        ans = []
        current = 0
        i,j = 0,0
       
        while i <= len(nums1)-1 and j <= len(nums2)-1:
            if nums1[i] <= nums2[j]:
                if current == keepTrack: 
                    ans.append(nums1[i])
                    keepTrack += 1
                i += 1
                current += 1
            else:
                if current == keepTrack:
                    ans.append(nums2[j])
                    keepTrack += 1
                j += 1
                current += 1
            if len(ans) == 2:
                break
        while i <= len(nums1)-1 and len(ans)!=2:
            
            if current == keepTrack: 
                ans.append(nums1[i])
                keepTrack += 1
            current += 1
            i += 1
        while j <= len(nums2)-1 and len(ans)!=2:
            
            if current == keepTrack: 
                ans.append(nums2[j])
                keepTrack += 1
            current += 1
            j += 1
        
        return float(ans[-1]) if medianCount % 2 else sum(ans)/2


         
        