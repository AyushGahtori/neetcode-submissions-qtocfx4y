class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(nums) - 1:
            maxjump = 0
            for i in range(l, r + 1):
                maxjump = max(maxjump, i + nums[i]) # i + nums[i] tells us at which index we can jump to.
            l = r + 1
            r = maxjump
            res += 1 # 1 loop = 1 jump
        return res        


        