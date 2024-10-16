
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def can_make_bouquets(day):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                        if bouquets == m:
                            return True
                else:
                    flowers = 0
            return False

        left, right = min(bloomDay), max(bloomDay)
        ans = -1 
        while left <= right:
            mid = (left + right) // 2
            if can_make_bouquets(mid):
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        
        return ans

        