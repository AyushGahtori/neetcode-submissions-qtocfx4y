# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

"""
EXAMPLE WALKTHROUGH FOR reverseKGroup
k = 2
head = [1, 2, 3, 4, 5]

Initial setup:
dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
groupPrev = dummy

------------------------------------
OUTER LOOP ITERATION 1
------------------------------------

getKth(groupPrev, 2):
- start at dummy
- move 2 steps -> node with value 2
kth = 2

groupNext = kth.next = 3

Group to reverse: [1 -> 2]

Initialize:
prev = groupNext = 3
curr = groupPrev.next = 1

Inner reversal loop (while curr != groupNext):

Iteration 1:
curr = 1
tmp = 2
1.next = 3
prev = 1
curr = 2

Iteration 2:
curr = 2
tmp = 3
2.next = 1
prev = 2
curr = 3 == groupNext -> stop

Reversed group is now: 2 -> 1 -> 3 -> 4 -> 5

Reconnect group:
tmp = groupPrev.next = 1
groupPrev.next = kth = 2
groupPrev = tmp = 1

List now:
dummy -> 2 -> 1 -> 3 -> 4 -> 5
groupPrev -> 1

------------------------------------
OUTER LOOP ITERATION 2
------------------------------------

getKth(groupPrev, 2):
- start at 1
- move 2 steps -> node with value 4
kth = 4

groupNext = kth.next = 5

Group to reverse: [3 -> 4]

Initialize:
prev = groupNext = 5
curr = groupPrev.next = 3

Inner reversal loop:

Iteration 1:
curr = 3
tmp = 4
3.next = 5
prev = 3
curr = 4

Iteration 2:
curr = 4
tmp = 5
4.next = 3
prev = 4
curr = 5 == groupNext -> stop

Reversed group is now: 4 -> 3 -> 5

Reconnect group:
tmp = groupPrev.next = 3
groupPrev.next = kth = 4
groupPrev = tmp = 3

List now:
dummy -> 2 -> 1 -> 4 -> 3 -> 5
groupPrev -> 3

------------------------------------
OUTER LOOP ITERATION 3
------------------------------------

getKth(groupPrev, 2):
- start at 3
- move 1 step -> 5
- move 1 step -> None
kth = None

Since kth is None:
break out of loop

------------------------------------
FINAL RESULT
------------------------------------

Return dummy.next

Final list:
2 -> 1 -> 4 -> 3 -> 5
"""

