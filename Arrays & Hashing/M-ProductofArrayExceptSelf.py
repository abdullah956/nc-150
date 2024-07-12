from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        # Step 1: Initialize prefix and postfix arrays
        prefix = [1] * length  # Space: O(n)
        postfix = [1] * length  # Space: O(n)
        res = [1] * length  # Space: O(n)

        # Step 2: Calculate prefix products
        for i in range(1, length):  # Time: O(n)
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Step 3: Calculate postfix products
        for i in range(length - 2, -1, -1):  # Time: O(n)
            postfix[i] = postfix[i + 1] * nums[i + 1]

        # Step 4: Calculate the result by multiplying prefix and postfix products
        for i in range(length):  # Time: O(n)
            res[i] = prefix[i] * postfix[i]

        return res  # Return the result array

"""
Time Complexity:
- The first loop runs in O(n) to compute the prefix products.
- The second loop runs in O(n) to compute the postfix products.
- The third loop runs in O(n) to combine the prefix and postfix products.
- Overall, the algorithm runs in O(n) time.

Space Complexity:
- The space complexity is O(n) due to the `prefix`, `postfix`, and `res` arrays, each of which stores n elements.
- The total space complexity is O(3n), which simplifies to O(n) in Big-O notation.
"""
