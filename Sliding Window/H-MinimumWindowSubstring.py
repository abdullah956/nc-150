class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Edge case: If t is empty, return an empty string
        if t == "":
            return ""

        # Dictionary to count the frequency of each character in t
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        # Dictionary to count the frequency of characters in the current window of s
        window = {}

        # Variables to keep track of the number of characters we have matched
        have, need = 0, len(countT)
        # Result variables: res will store the indices of the minimum window, resLen will store its length
        res, resLen = [-1, -1], float("infinity")
        # Left pointer for the sliding window
        l = 0

        # Iterate through s with the right pointer r
        for r in range(len(s)):
            char = s[r]
            # Update the count of the current character in the window
            window[char] = 1 + window.get(char, 0)

            # If the current character is needed and the count matches the required count, increment have
            if char in countT and window[char] == countT[char]:
                have += 1

            # While we have all the characters needed
            while have == need:
                # Check if the current window is smaller than the previously recorded smallest window
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # Pop the leftmost character from the window
                window[s[l]] -= 1
                # If the popped character is needed and the window no longer has enough of it, decrement have
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # Move the left pointer to the right
                l += 1

        # Extract the substring of the minimum window, if one was found
        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
