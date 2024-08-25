class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        hashMap = {}
        ans = 0
        for i, fruit in enumerate(fruits):
            if fruit not in hashMap:
                hashMap[fruit] = 1
            else:
                hashMap[fruit] += 1
            while len(hashMap) > 2:
                hashMap[fruits[left]] -= 1
                if hashMap[fruits[left]] == 0:
                    del hashMap[fruits[left]]
                left += 1
            ans = max(ans, i-left + 1)

        return ans
            
            
            
        