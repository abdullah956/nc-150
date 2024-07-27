class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters.

        Time Complexity: O(n) where n is the length of the input string s.
        Space Complexity: O(min(n, m)) where n is the length of the input string and m is the size of the character set.
        """
        res = 0  # Initialize the result to store the maximum length of substring found.
        l = 0  # Left pointer for the sliding window.
        SET = set()  # Set to store characters in the current window without duplicates.

        # Iterate over the string with the right pointer.
        for r in range(len(s)):
            # If the character at the right pointer is already in the set, remove characters from the left.
            while s[r] in SET:
                SET.remove(s[l])  # Remove the character at the left pointer from the set.
                l += 1  # Move the left pointer to the right.

            # Add the character at the right pointer to the set.
            SET.add(s[r])
            # Update the result with the maximum length of the current window.
            res = max(res, r - l + 1)
        
        return res  # Return the length of the longest substring without repeating characters.
