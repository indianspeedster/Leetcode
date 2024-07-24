class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapper = {str(i):str(j) for i,j in enumerate(mapping)}
        num2 = [str(i) for i in nums]
        num2 = [list(i) for i in num2]
     
        num2 = [[mapper[i] for i in num] for num in num2]
        num2 = [int("".join(i)) for i in num2]
        arr = zip(nums, num2)
        arr = sorted(arr, key = lambda x : x[1] )
        return [ar for ar, br in arr]
        