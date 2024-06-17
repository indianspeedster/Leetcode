class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        k = int(c **0.5)
        
        for i in range(k+1):
            left, right = i, k
            while left <= right:
                mid = (left + right)//2
                num = (i + mid) ** 2 - 2*i*mid
                if num == c:
                    return True
                if num > c:
                    right = mid-1
                else:
                    left = mid + 1
        return False
                
            
        