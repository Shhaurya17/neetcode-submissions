class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ha = {}
        diff = 0
        ans = []
        for i in range(len(nums)):
            ha[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in ha and ha[diff] != i:
                ans.append(i)
                ans.append(ha[diff])
                return sorted(ans)
            else:
                continue