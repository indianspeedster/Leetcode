class Solution:
    def customSortString(self, order: str, s: str) -> str:
        arrayS = list(s)
        curIndex = 0
        for element in order:
            for ind, ele in enumerate(arrayS):
                if ele == element:
                    arrayS[ind], arrayS[curIndex] = arrayS[curIndex], arrayS[ind]
                    curIndex += 1
        return "".join(arrayS)

        
        