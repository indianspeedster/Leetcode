class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        left = []
        for i in height:
            left.append(leftmax)
            leftmax = max(i, leftmax)
        rightmax = 0
        right = []
        for i in height[::-1]:
            right.append(rightmax)
            rightmax = max(rightmax, i)
        right = right[::-1]
        ans = 0
    
 
        for i, heigh in enumerate(height):
            ans += max(0, min(left[i],right[i]) - heigh)
       
        return ans
        
        