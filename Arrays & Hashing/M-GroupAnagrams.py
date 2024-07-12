from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold sorted string as keys and list of anagrams as values
        anagram_groups = defaultdict(list)
        
        for s in strs:
            # Sort the string to form the key
            sorted_str = ''.join(sorted(s))
            # Append the original string to the list corresponding to the sorted key
            anagram_groups[sorted_str].append(s)
        
        # Return the values of the dictionary as a list of lists
        return list(anagram_groups.values())

        # Time complexity: O(n * k log k)
        # We iterate through each string in the list (O(n)), and for each string,
        # we sort it which takes O(k log k) where k is the maximum length of a string.
        
        # Space complexity: O(n * k)
        # We store each string in the dictionary, and in the worst case, 
        # we store each character of each string, hence O(n * k).
        # Dictionary to hold the count tuple as keys and list of anagrams as values

        
        res = defaultdict(list)
        
        for s in strs:
            # Initialize a count array for each letter in the alphabet
            count = [0] * 26
            
            # Count occurrences of each character in the string
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Use the tuple of counts as the key
            res[tuple(count)].append(s)
        
        # Return the values of the dictionary as a list of lists
        return list(res.values())

        # Time complexity: O(n * k)
        #   - n is the number of strings in strs
        #   - k is the maximum length of a string in strs
        #   - Counting characters in each string takes O(k) time,
        #     and we do this for each of the n strings.
        
        # Space complexity: O(n * k)
        #   - We store each string in the dictionary, and in the worst case,
        #     we store each character of each string in the count array,
        #     resulting in O(n * k) space usage.