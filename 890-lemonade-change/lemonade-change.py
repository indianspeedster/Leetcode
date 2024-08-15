class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5:0, 10:0, 20:0}
        for bill in bills:
            if bill == 5:
                dic[5] += 1
            if bill == 10:
                if dic[5]>=1:
                    dic[5]-=1
                else:
                    return False
                dic[10] += 1
            if bill == 20:
                if dic[5] >=1 and dic[10]>=1:
                    dic[5] -= 1
                    dic[10] -= 1
                    dic[20] += 1
                elif dic[5]>=3:
                    dic[5] -=3
                    dic[20] += 1
                else:
                    return False
        return True        