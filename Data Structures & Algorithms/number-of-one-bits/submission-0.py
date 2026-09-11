class Solution:
    def hammingWeight(self, n: int) -> int:
        b = str(bin(n))
        return b.count("1")