from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time Complexity: O(log n), where n is the number of elements in nums
        # Space Complexity: O(1), since we are using only a constant amount of extra space

        # Initialize the start and end pointers
        start, end = 0, len(nums) - 1
        # Initialize the current minimum to infinity
        curr_min = float("inf")
        
        # Perform binary search to find the minimum element
        while start < end:
            # Calculate the midpoint
            mid = start + (end - start) // 2
            # Update the current minimum with the midpoint value
            curr_min = min(curr_min, nums[mid])
            
            # If the right half has the minimum element
            if nums[mid] > nums[end]:
                start = mid + 1
            # If the left half has the minimum element
            else:
                end = mid - 1
        
        # Return the minimum of the current minimum and the element at the start pointer
        return min(curr_min, nums[start])
