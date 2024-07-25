from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Find the median of two sorted arrays.

        Time Complexity: O((m + n) log(m + n)) where m is the length of nums1 and n is the length of nums2.
        Space Complexity: O(m + n) for storing the merged array.
        """
        merged = []  # Initialize the merged list.
        sum = 0  # Initialize the sum to calculate the median.
        
        # Append all elements from nums1 to the merged list.
        for val in nums1:
            merged.append(val)
        
        # Append all elements from nums2 to the merged list.
        for val in nums2:
            merged.append(val)
        
        # Sort the merged list.
        merged = sorted(merged)
        
        # If the length of the merged list is even.
        if len(merged) % 2 == 0:
            # Reduce the list to the two middle elements.
            while len(merged) > 2:
                merged.pop(0)
                merged.pop(-1)
        else:
            # Reduce the list to the single middle element.
            while len(merged) > 1:
                merged.pop(0)
                merged.pop(-1)
        
        # Calculate the sum of the remaining element(s).
        for digit in merged:
            sum += digit
        
        # Return the average of the remaining element(s) as the median.
        return float(sum) / len(merged)
