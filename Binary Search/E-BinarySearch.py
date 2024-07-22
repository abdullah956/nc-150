from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Initialize the left and right pointers
        l = 0
        r = len(nums) - 1

        # Loop until the pointers cross
        while l <= r:
            # Calculate the midpoint
            mid = (l + r) // 2

            # If the midpoint value is less than the target, adjust the left pointer
            if nums[mid] < target:
                l = mid + 1
            # If the midpoint value is greater than the target, adjust the right pointer
            elif nums[mid] > target:
                r = mid - 1
            # If the target is found, return the index
            else:
                return mid

        # If the target is not found, return -1
        return -1

# Time Complexity: O(log n)
# Space Complexity: O(1)