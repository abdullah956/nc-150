from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Resultant list to store the maximums
        res = []
        
        # Iterate over each possible starting index of the window
        for i in range(len(nums) - k + 1):
            # Find the maximum in the current window
            max_val = max(nums[i:i + k])
            # Append the maximum to the result list
            res.append(max_val)
        
        return res
    

