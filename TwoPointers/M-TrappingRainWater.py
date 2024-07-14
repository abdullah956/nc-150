from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:  # Check if the height list is empty
            return 0
        
        l, r = 0, len(height) - 1  # Initialize two pointers, l at the start and r at the end
        leftMax, rightMax = height[l], height[r]  # Initialize variables to track the maximum heights from left and right
        res = 0  # Initialize the variable to store the total trapped water
        
        while l < r:  # Continue until the two pointers meet
            if leftMax < rightMax:  # If the left boundary is lower than the right boundary
                l += 1  # Move the left pointer to the right
                leftMax = max(leftMax, height[l])  # Update the leftMax if a higher wall is found
                res += leftMax - height[l]  # Calculate and add trapped water based on the updated leftMax
            else:  # If the right boundary is lower than or equal to the left boundary
                r -= 1  # Move the right pointer to the left
                rightMax = max(rightMax, height[r])  # Update the rightMax if a higher wall is found
                res += rightMax - height[r]  # Calculate and add trapped water based on the updated rightMax
        
        return res  # Return the total trapped water

# Time Complexity: O(n) - Each element is visited once by each pointer, so the time complexity is linear.
# Space Complexity: O(1) - Only a few variables are used to store indices, maximum heights, and the result,
# regardless of the input size.
