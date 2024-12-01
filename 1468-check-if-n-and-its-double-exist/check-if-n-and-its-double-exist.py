class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        map1 = set()

        nums = [float(i) for i in arr]

        for num in nums:
            double = num *2
            half = num / 2
           
            if num in map1 :
                return True
            map1.add(half)
            map1.add(double)
        return False
        