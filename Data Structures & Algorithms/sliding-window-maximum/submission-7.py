import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()  # stores indices
        l = r = 0

        while r < len(nums):
            # Pop smaller values from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove leftmost index if it's out of window
            if q[0] < l:
                q.popleft()

            # Once window size is reached, record max
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
