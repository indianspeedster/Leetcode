class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        handd = Counter(hand)
        arr = list(handd.keys())
        heapq.heapify(arr)
        while arr:
            ele = arr[0]
            for i in range(ele, ele+groupSize):
                if i not in handd:
                    return False
                handd[i] -= 1
                if handd[i] == 0:
                    
                    heapq.heappop(arr)
        return True

        







        