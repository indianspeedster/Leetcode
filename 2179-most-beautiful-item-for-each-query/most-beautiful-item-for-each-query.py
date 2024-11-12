class Solution:
    def maximumBeauty(
        self, items: List[List[int]], queries: List[int]
    ) -> List[int]:
        items.sort(key = lambda x: x[0])

        maxBeauty = items[0][1]

        for i, item in enumerate(items):
            maxBeauty = max(maxBeauty, item[1])
            items[i][1] = maxBeauty
        
        return [self.binarySearch(items, query) for query in queries]
    

    def binarySearch(self, items, target):
        left, right = 0, len(items)-1
        maxBeauty = 0
        while left <= right:
            mid = (left+right) // 2

            if items[mid][0] > target:
                right = mid-1
            else:
                maxBeauty = max(maxBeauty, items[mid][1])
                left = mid+1
        return maxBeauty