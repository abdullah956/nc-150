class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths of the two strings are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Initialize a dictionary to store the count of each character in s
        char_count = dict()
        
        # Count each character in the first string s
        for c in s:
            if c not in char_count:
                # If the character is not in the dictionary, add it with a count of 1
                char_count[c] = 1
            else:
                # If the character is already in the dictionary, increment its count
                char_count[c] += 1
        
        # Subtract the count for each character in the second string t
        for c in t:
            if c in char_count:
                # If the character is in the dictionary, decrement its count
                char_count[c] -= 1
                # If the count goes below 0, it means t has more occurrences of this character than s
                if char_count[c] < 0:
                    return False
            else:
                # If the character is not in the dictionary, s does not have this character
                return False
        
        # If all counts are zero, then s and t are anagrams
        return True

        # Time complexity: O(n)
        # We iterate through both strings s and t, which takes O(n) time where n is the length of the strings.
        
        # Space complexity: O(1)
        # The space complexity is O(1) because the size of the char_count dictionary is bounded by the number of possible characters (in this case, the English alphabet), which is constant.
