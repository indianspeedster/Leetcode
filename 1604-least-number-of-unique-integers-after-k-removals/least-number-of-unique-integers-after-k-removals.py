class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        element_dic = Counter(arr)
        ind = 0
        for key, val in sorted(element_dic.items(), key = lambda x : x[1]):
            if k >= val:
                k -= val
                ind += 1
            else:
                return len(element_dic) - ind
        
        return 0