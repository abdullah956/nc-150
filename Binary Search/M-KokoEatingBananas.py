import math
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time Complexity: O(n log max(piles)), where n is the number of elements in piles
        # Space Complexity: O(1), since we are using only a constant amount of extra space

        # Initialize the left and right pointers for binary search
        l, r = 1, max(piles)
        # Initialize the result variable to the maximum possible speed
        res = r

        # Perform binary search to find the minimum eating speed
        while l <= r:
            # Calculate the midpoint (current eating speed)
            k = (l + r) // 2

            # Calculate the total time required to eat all the bananas at speed k
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            
            # If the total time is within the given hours, update the result and adjust the right pointer
            if totalTime <= h:
                res = k
                r = k - 1
            # If the total time exceeds the given hours, adjust the left pointer
            else:
                l = k + 1
        
        # Return the minimum eating speed
        return res
