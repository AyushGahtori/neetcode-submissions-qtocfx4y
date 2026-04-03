class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0 

        l, r = 0, len(height) - 1
        maxleft, maxright = height[l], height[r]
        water = 0

        while l < r:
            if maxleft < maxright:
                l += 1
                maxleft  = max(maxleft, height[l])
                water = water + (maxleft - height[l])
            else:
                r -= 1
                maxright = max(maxright, height[r])
                water = water + (maxright - height[r])
        return water            

        