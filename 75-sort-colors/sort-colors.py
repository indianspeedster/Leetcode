class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        k = len(nums)-1

        while i <= k:
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i+=1
                
            elif nums[i] == 2:
                nums[i], nums[k] = nums[k], nums[i]
                k -= 1
                
            else:
                i += 1
            
        

            

