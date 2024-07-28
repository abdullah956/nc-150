class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the length of the longest substring that can be obtained by replacing at most 'k' characters.
        """
        count = {}  # Dictionary to store the count of each character in the current window.
        max_length = 0  # Maximum length of the valid window.
        max_count = 0  # Maximum count of any single character in the current window.
        left = 0  # Left pointer for the sliding window.

        # Iterate over the string with the right pointer.
        for right in range(len(s)):
            char_right = s[right]
            count[char_right] = count.get(char_right, 0) + 1  # Increment the count of the current character.
            max_count = max(max_count, count[char_right])  # Update the maximum character count in the window.
            
            # Calculate the current window size.
            window_size = right - left + 1

            # If we need to replace more than 'k' characters, shrink the window from the left.
            if window_size - max_count > k:
                char_left = s[left]
                count[char_left] -= 1  # Decrement the count of the character at the left pointer.
                left += 1  # Move the left pointer to the right.
            
            # Update the maximum length of the window.
            max_length = max(max_length, right - left + 1)

        return max_length  # Return the size of the largest valid window.
