from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # Initialize the result list
        nums.sort()  # Sort the array to facilitate the two-pointer approach
        
        for i, v in enumerate(nums):
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and v == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1  # Initialize two pointers
            
            while l < r:
                sum = v + nums[l] + nums[r]  # Calculate the sum of the triplet
                
                if sum > 0:
                    r -= 1  # Move the right pointer left if the sum is too large
                elif sum < 0:
                    l += 1  # Move the left pointer right if the sum is too small
                else:
                    res.append([v, nums[l], nums[r]])  # Add the valid triplet to the result
                    l += 1  # Move the left pointer right to find the next unique element
                    # Skip duplicate elements to avoid duplicate triplets
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res  # Return the list of triplets

# Time Complexity: O(n^2) - The outer loop runs in O(n) time and the inner while loop runs in O(n) time for each iteration of the outer loop.
# Space Complexity: O(n) - The space complexity is dominated by the space required for the output list, which can store up to O(n^3) triplets in the worst case.
