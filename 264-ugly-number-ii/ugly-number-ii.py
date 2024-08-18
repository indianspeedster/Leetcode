class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hashset = set([1])
        count = 0
        arr = [1]
        heapq.heapify(arr)
        while True:
            element = heapq.heappop(arr)
            count += 1
            if count == n:
                return element
            num1, num2, num3 = element*2, element*3, element*5
            if num1 not in hashset:
                hashset.add(num1)
                heapq.heappush(arr, num1)
            if num2 not in hashset:
                hashset.add(num2)
                heapq.heappush(arr, num2)
            if num3 not in hashset:
                hashset.add(num3)
                heapq.heappush(arr, num3)
            

        