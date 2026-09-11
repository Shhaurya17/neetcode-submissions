class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b:
            carry = (a&b)<<1
            a = (a^b) & mask
            b= carry & mask
        if a <= MAX_INT :
            return a
        else: 
            return ~(a^mask)