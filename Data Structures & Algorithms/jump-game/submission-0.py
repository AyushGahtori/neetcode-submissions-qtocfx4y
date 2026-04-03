"""
Solution 1: (brute force.)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def dfs(i):

            # Base case: if we are at or beyond the last index, we can reach the end
            if i>= len(nums) -1:
                return True

            # Calculate maxJump: the farthest we can go from the current position i
            # maxJump determines the farthest position we can reach from the current position i.
            # The calculation i + nums[i] represents the maximum index we can jump to from i.
            # We use min(i + nums[i], len(nums) - 1) to ensure maxJump doesn’t go beyond the last index.
            # example nums = [3, 2, 1, 0, 4] when i = 0 nums[i] = 3 so i + nums[i] = 0 +3 = 3
            # there fore we can jump to index 1, 2, 3.
            maxJump = min(i + nums[i], len(nums) - 1)

            # Try every possible jump from the next position (i+1) up to maxJump
            # i + 1 = next position from the current one.
            # maxjump + 1 because the its inclusive so if i is 0 and maxjump is 3.
            # we try jumping on to the index 1, 2, 3.
            for nextPosition in range(i + 1, maxJump + 1): 
                if dfs(nextPosition): # if def(nextPosition) = True 
                    return True # means there is a path to the end from the current position i.

            # dealing with dead-end
            # A 0 at any position means nums[i] = 0, so maxJump = i
            # which leads to an empty range in the for loop (range(i + 1, i + 1))
            # effectively making dfs(i) return False.
            return False 

        return dfs(0)  
"""   

# solution 2 (greedy)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 # gives us the index where goal is
        for i in range(len(nums) - 1, -1, -1): # itterate ove the nums array backwords
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False        


        