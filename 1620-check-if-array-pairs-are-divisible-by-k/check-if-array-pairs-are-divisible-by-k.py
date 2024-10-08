class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hashSet = defaultdict(int)
        for i in arr:
            modval = i % k
            if modval == 0:
                if hashSet[0] > 0:
                    hashSet[0] -= 1
                else:
                    hashSet[0] += 1
            elif hashSet[k-modval] > 0:
                hashSet[k-modval] -= 1
            else:
                hashSet[modval] += 1
        return sum(hashSet.values()) == 0
        