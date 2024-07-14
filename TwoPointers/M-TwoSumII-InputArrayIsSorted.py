from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Initialize two pointers

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1  # Move right pointer left
            elif curSum < target:
                l += 1  # Move left pointer right
            else:
                return [l + 1, r + 1]  # Return 1-based indices

# Time Complexity: O(n) - Each element is processed at most once.
# Space Complexity: O(1) - Only a constant amount of extra space is used.
