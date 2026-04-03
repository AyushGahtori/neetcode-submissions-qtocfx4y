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
            if i + nums[i] >= goal: # Check if from index i, we can reach or exceed the current goal
                goal = i
        return True if goal == 0 else False  


"""
Let's perform a dry run on an example where it is possible to reach the goal. We’ll use nums = [2, 3, 1, 1, 4].

Dry Run Example
Let’s go through each step to see how the goal moves as we iterate backward.

Initial State:

goal = 4 (last index)
Iteration 1 (i = 4):

i + nums[i] = 4 + 4 = 8, which is greater than or equal to goal = 4.
So, we update goal = 4 (unchanged because i is already 4).
Iteration 2 (i = 3):

i + nums[i] = 3 + 1 = 4, which is equal to goal = 4.
Since we can reach goal from index 3, we update goal = 3.
Iteration 3 (i = 2):

i + nums[i] = 2 + 1 = 3, which is equal to goal = 3.
Since we can reach goal from index 2, we update goal = 2.
Iteration 4 (i = 1):

i + nums[i] = 1 + 3 = 4, which is greater than or equal to goal = 2.
Since we can reach goal from index 1, we update goal = 1.
Iteration 5 (i = 0):

i + nums[i] = 0 + 2 = 2, which is greater than or equal to goal = 1.
Since we can reach goal from index 0, we update goal = 0.
"""



        