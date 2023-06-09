class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,h = 0,len(nums)-1
        arr=nums
        while l<=h:
            mid = (l+h)//2
            if arr[mid]==target:
                return True
            elif arr[mid]==arr[l]==arr[h]:
                l = l+1
                h = h-1
            elif arr[mid]>=arr[l]:
                if target>=arr[l] and target<arr[mid]:
                    h = mid-1
                else:
                    l = mid + 1
            else:
                if target>arr[mid] and target<=arr[h]:
                    l = mid + 1
                else:
                    h = mid-1
        return False
        