class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        stack = []
        curr = [i for i in range(len(deck))]
        ans = [0 for i in range(len(deck))]
        sortedArray = sorted(deck, reverse=True)
        pick = True
        while curr:
            for cur in curr:
                if pick and sortedArray:
                    element = sortedArray.pop()
                    ans[cur] = element
                    pick = False
                else:
                    stack.append(cur)
                    pick = True
            curr = stack
            stack = []
        return ans


        