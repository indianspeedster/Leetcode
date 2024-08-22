class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)
        a = list(a[2:])
        for i, char in enumerate(a):
            if char == "0":
                a[i] = "1"
            else:
                a[i] = "0"
        return int("".join(a),2)
        