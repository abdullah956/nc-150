from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0  # Initialize maxArea to store the maximum area found
        stack = []  # Initialize an empty stack to store pairs of (index, height)

        # Iterate through each bar in the histogram
        for i, h in enumerate(heights):
            start = i  # Start index for the current bar
            # While the stack is not empty and the current height is less than the height at the top of the stack
            while stack and stack[-1][1] > h:
                index, height = stack.pop()  # Pop the top of the stack
                # Calculate the area with the popped height as the smallest height
                maxArea = max(maxArea, height * (i - index))
                start = index  # Update the start index
            # Append the current bar's start index and height to the stack
            stack.append((start, h))

        # Process remaining bars in the stack
        for i, h in stack:
            # Calculate the area with the remaining heights in the stack
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea  # Return the maximum area found

# Time Complexity: O(n), where n is the number of bars in the histogram.
# Each bar is pushed and popped from the stack at most once.

# Space Complexity: O(n), where n is the number of bars in the histogram.
# The stack can contain all the bars in the worst case.