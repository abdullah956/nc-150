from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty set to store unique numbers
        seen = set()
        
        # Iterate through each number in the input list
        for n in nums:
            # Check if the number is already in the set
            if n in seen:
                # If found, return True since there's a duplicate
                return True
            # Add the number to the set
            seen.add(n)
        
        # If no duplicates are found, return False
        return False

        # Time complexity: O(n)
        # We iterate through each of the n elements once, and each set operation (add, in) is O(1) on average.

        # Space complexity: O(n)
        # In the worst case, where there are no duplicates, we store all n elements in the set.
