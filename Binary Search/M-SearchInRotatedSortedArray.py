from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers for the start and end of the list
        l, r = 0, len(nums) - 1

        # Continue searching while the left pointer is less than or equal to the right pointer
        while l <= r:
            # Calculate the mid index
            mid = (l + r) // 2

            # Check if the target is at the mid index
            if target == nums[mid]:
                return mid  # Target found, return the index

            # Determine if the left portion is sorted
            if nums[l] <= nums[mid]:
                # If the target is greater than mid element or less than the left element,
                # then the target must be in the right half
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1  # Move the left pointer to the right of mid
                else:
                    r = mid - 1  # Otherwise, move the right pointer to the left of mid
            # Right portion must be sorted
            else:
                # If the target is less than mid element or greater than the right element,
                # then the target must be in the left half
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1  # Move the right pointer to the left of mid
                else:
                    l = mid + 1  # Otherwise, move the left pointer to the right of mid

        # Target not found, return -1
        return -1

# Time Complexity: O(log n) - The binary search algorithm reduces the search space by half in each iteration.
# Space Complexity: O(1) - The space complexity is constant because no extra space is used that grows with the input size.
