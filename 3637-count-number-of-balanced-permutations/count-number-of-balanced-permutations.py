class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10 ** 9 + 7
        arr = [int(x) for x in num]
        N = len(arr)
        M = 0

        f = [0] * 10
        for x in arr:
            f[x] += 1
            M += x

        if M % 2 != 0:
            return 0
            
        fact = [1]
        ifact = [pow(1, -1, MOD)]
        for i in range(1, N + 1):
            fact.append((fact[-1] * i) % MOD)
            ifact.append(pow(fact[-1], -1, MOD))

        numer = 1
        if N % 2 == 0:
            numer = (fact[(N // 2)] * fact[(N // 2)]) % MOD
        else:
            numer = (fact[((N + 1) // 2)] * fact[(N // 2)]) % MOD
            
        @cache
        def go(index, left_count, left_sum):
            if left_count < 0 or left_sum < 0:
                return 0
            if index == len(f):
                if left_count != 0 or left_sum != 0:
                    return 0
                return 1
        
            total = 0
            for i in range(f[index] + 1):
                # on the left side, we put i "index" digit on the left
                left = i
                # the rest on the right
                right = f[index] - i
                total += go(index + 1, left_count - left, left_sum - (left * index)) * ifact[left] * ifact[right]
                total %= MOD
            return total % MOD
        
        return (go(0, (N + 1) // 2, M // 2) * numer) % MOD
        