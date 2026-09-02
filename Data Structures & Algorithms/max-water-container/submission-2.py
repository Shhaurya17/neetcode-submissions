class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights) -1
        res = 0
    
        while l<r :
            wid = r-l
            curr = wid*min(heights[l],heights[r])
            if heights[l] <= heights[r] :
                l+=1
            else:
                r-=1
            res = max(res,curr)
        return res

