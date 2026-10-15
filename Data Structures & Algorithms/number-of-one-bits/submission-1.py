class Solution:
    def hammingWeight(self, n: int) -> int:
        # binary = bin(n)
        # count = binary.count("1")
        # return count
        res = 0
        for i in range(32):
            if (1 << i) & n:
                res += 1
        return res