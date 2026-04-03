class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxv = 0
        l, r = 0, len(heights) - 1
        while l<r:
            currv = (r - l) * min(heights[l], heights[r])
            maxv = max(maxv, currv)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxv            

