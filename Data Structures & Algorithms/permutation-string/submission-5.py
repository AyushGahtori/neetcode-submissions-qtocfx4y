class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # -------------------------
        # Step 1: Edge case
        # -------------------------
        if len(s1) > len(s2):
            return False  # impossible
        
        # --------------------------------------------------------------
        # Step 2: Build hashmap frequency counts of s1 and first window
        # --------------------------------------------------------------
        from collections import defaultdict

        s1Count = defaultdict(int)  # frequency of chars in s1
        winCount = defaultdict(int) # frequency of chars in current window of s2

        # fill s1Count
        for ch in s1:
            s1Count[ch] += 1

        # fill winCount for the very first window of size len(s1)
        windowSize = len(s1)
        for i in range(windowSize):
            winCount[s2[i]] += 1

        # -------------------------------------------------------------------
        # Step 3: count how many characters currently have matching frequency
        # -------------------------------------------------------------------
        matches = 0
        # For every character in s1Count, check if freq matches in winCount.
        for ch in s1Count:
            if s1Count[ch] == winCount[ch]:
                matches += 1

        # At this moment:
        # - matches = number of characters whose freq in window == freq in s1.
        # - If matches == size of hashmap (all chars match), it's a permutation.

        # -------------------------------------------------------
        # Step 4: Slide the window across s2 one char at a time
        # -------------------------------------------------------
        left = 0    # left pointer of window

        for right in range(windowSize, len(s2)):
            # If all characters match → window is a permutation
            if matches == len(s1Count):
                return True

            # ----------------------------
            # Add the new character (s2[right])
            # ----------------------------
            newChar = s2[right]

            # Before increasing, check if increasing breaks or forms a match
            if newChar in s1Count:
                # If new freq becomes EXACTLY equal to s1Count → one more match
                if winCount[newChar] + 1 == s1Count[newChar]:
                    matches += 1
                # If freq WAS matching before and now becomes mismatched → minus one match
                elif winCount[newChar] == s1Count[newChar]:
                    matches -= 1

            # Actually update freq
            winCount[newChar] += 1

            # ----------------------------
            # Remove old character (s2[left])
            # ----------------------------
            oldChar = s2[left]

            if oldChar in s1Count:
                # If freq WAS equal and now becomes unequal → lose a match
                if winCount[oldChar] == s1Count[oldChar]:
                    matches -= 1
                # If freq AFTER removal becomes equal → regain a match
                elif winCount[oldChar] - 1 == s1Count[oldChar]:
                    matches += 1

            winCount[oldChar] -= 1  # actually remove the character from window
            left += 1  # slide window forward

        # Final check for the last window
        return matches == len(s1Count)
