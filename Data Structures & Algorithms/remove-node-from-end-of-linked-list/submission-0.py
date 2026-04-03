class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        # --------------------------
        # Step 1: Reverse the list
        # --------------------------
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev is now the head of the reversed list

        # --------------------------
        # Step 2: Reverse back, skipping the nth node
        # --------------------------
        count = 1       # count positions in reversed list
        curr = prev     # start of reversed list
        prev2 = None    # new list head (re-reversed)
        
        while curr:
            nxt = curr.next

            if count == n:
                # skip this node (do NOT attach curr)
                curr = nxt
                count += 1
                continue

            # normal reverse step
            curr.next = prev2
            prev2 = curr
            curr = nxt
            count += 1
        
        return prev2
               
