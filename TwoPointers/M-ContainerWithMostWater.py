from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1  # Initialize two pointers, l at the start and r at the end of the list
        res = 0  # Initialize the result variable to store the maximum area found

        while l < r:  # Continue the loop while the left pointer is less than the right pointer
            # Calculate the area with the current left and right pointers
            res = max(res, min(height[l], height[r]) * (r - l))
            
            # Move the pointer pointing to the shorter line
            if height[l] < height[r]:
                l += 1  # Move the left pointer to the right if the left height is less
            else:
                r -= 1  # Move the right pointer to the left if the right height is less or equal
        
        return res  # Return the maximum area found

# Time Complexity: O(n) - Each element is visited at most once, as the pointers only move towards each other.
# Space Complexity: O(1) - Only a few variables are used for storing indices and the result, regardless of the input size.
