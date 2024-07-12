from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  # Convert nums into a set for O(1) average time complexity in lookups
        longest = 0

        for n in numSet:
            # Check if n is the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                # Calculate the length of the consecutive sequence starting from n
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)  # Update the longest length found
        
        return longest
"""
Time Complexity: O(n)
- Creating numSet from nums: O(n)
- Iterating through each unique number in numSet: O(n)
- Inside the loop, while loop and set lookups are average O(1), contributing O(n) in worst-case scenarios.

Space Complexity: O(n)
- numSet: O(n) for storing all unique elements from nums.
- Other variables (longest, length): O(1) constant space.

Therefore, the overall time complexity is O(n), and the overall space complexity is O(n).
"""
