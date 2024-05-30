

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        count = defaultdict(int)
        total = defaultdict(int)
        result = 0

        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        for k in range(n):
            if prefix_xor[k + 1] in count:
                result += count[prefix_xor[k + 1]] * k - total[prefix_xor[k + 1]]
            count[prefix_xor[k]] += 1
            total[prefix_xor[k]] += k

        return result

        