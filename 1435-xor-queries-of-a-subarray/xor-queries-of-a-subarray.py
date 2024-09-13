class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix_XOR = [0] * (n + 1)

       
        for i in range(n):
            prefix_XOR[i + 1] = prefix_XOR[i] ^ arr[i]

        result = []
        
        for q in queries:
            result.append(prefix_XOR[q[1] + 1] ^ prefix_XOR[q[0]])
        return result