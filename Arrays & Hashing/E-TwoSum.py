from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize a dictionary to store the complement and its index
        checklist = dict()
        
        # Iterate through each number in the list along with its index
        for i in range(len(nums)):
            num = nums[i]
            # Calculate the complement needed to reach the target
            complement = target - num
            
            # Check if the current number is in the dictionary (i.e., if its complement was previously encountered)
            if num in checklist:
                # If found, return the indices of the complement and the current number
                return [checklist[num], i]
            else:
                # Otherwise, store the complement and its index in the dictionary
                checklist[complement] = i
        
        # If no solution is found, return an empty list (optional, based on problem constraints)
        return []

        # Time complexity: O(n)
        # We iterate through the list once, and dictionary operations (insertion and lookup) are O(1) on average.
        
        # Space complexity: O(n)
        # In the worst case, we store each element in the dictionary, which takes O(n) space.
