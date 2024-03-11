class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = defaultdict(int)
        for c in s:
            counter[c] += 1

        sb = []
        for o in order:
            for i in range(counter[o]):
                sb.append(o)
            counter[o] = 0

        for key in counter:
                for i in range(counter[key]):
                    sb.append(key)
        
        return ''.join(sb)
        