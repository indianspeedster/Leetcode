class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        store = defaultdict(int)
        for num in arr:
            store[num] += 1
        vis = set()
        for val in store.values():
            if val in vis:
                return False
            vis.add(val)
        return True


        