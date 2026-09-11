class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = 0
        b=0
        n = len(nums)
        for i in range(n+1):
            b = b^i
        for j in nums:
            a = a^j
        return b^a