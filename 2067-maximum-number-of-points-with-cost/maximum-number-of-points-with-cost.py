class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        
       
        dp = points[0][:]
        
        for i in range(1, rows):
            left_max = [0] * cols
            right_max = [0] * cols
            new_dp = [0] * cols
            
         
            left_max[0] = dp[0]
            for j in range(1, cols):
                left_max[j] = max(left_max[j-1] - 1, dp[j])
            
           
            right_max[cols-1] = dp[cols-1]
            for j in range(cols-2, -1, -1):
                right_max[j] = max(right_max[j+1] - 1, dp[j])
            
            
            for j in range(cols):
                new_dp[j] = points[i][j] + max(left_max[j], right_max[j])
            
            dp = new_dp
        
        return max(dp)