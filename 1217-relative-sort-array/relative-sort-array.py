class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = defaultdict(lambda : 1001)
        for i,j in enumerate(arr2):
            dic[j] = i
        arr = sorted(arr1, key=lambda x: (dic[x], x))
        return arr
        

