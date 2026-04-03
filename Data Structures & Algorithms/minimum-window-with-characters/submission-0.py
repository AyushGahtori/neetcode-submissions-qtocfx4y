class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        if len(t) == 0:
            return ""

        window, ct = {}, {}

        # Create a frequency map for characters in t
        for char in t:
            ct[char] = 1 + ct.get(char, 0)

        have, need = 0, len(ct)  # `need` should be the number of unique characters
        l = 0
        res = [-1, -1]
        reslen = float("inf")

        # Sliding window
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in ct and window[c] == ct[c]:
                have += 1

            while have == need:
                # Update result if current window is smaller
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res = [l, r]

                # Slide the window to the right
                window[s[l]] -= 1
                if s[l] in ct and window[s[l]] < ct[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        if reslen != float("inf"):
            return s[l : r + 1]
        else:
            return ""
