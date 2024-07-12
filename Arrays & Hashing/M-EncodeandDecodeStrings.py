from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        
        Time Complexity: O(n), where n is the total number of characters in all strings.
        Space Complexity: O(n), where n is the total number of characters in all strings.
        """
        res = ""
        for s in strs:
            # Append the length of the string, a delimiter '#', and the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back into a list of strings.
        
        Time Complexity: O(n), where n is the length of the encoded string.
        Space Complexity: O(n), where n is the length of the encoded string.
        """
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the delimiter to get the length of the next string
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Extract the length of the string
            i = j + 1  # Move past the delimiter
            j = i + length  # Find the end of the actual string
            res.append(s[i:j])  # Extract the string based on the length and append to the result
            i = j  # Move to the next encoded string
            
        return res