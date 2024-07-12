from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a dictionary to count frequencies of each number
        count = {}  # Space: O(n)
        
        # Count frequencies of each number in nums
        for n in nums:  # Time: O(n)
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        # Step 2: Initialize a list of lists to store numbers by their frequency
        freq = [[] for _ in range(len(nums) + 1)]  # Space: O(n)
        
        # Store numbers in freq list based on their frequency
        for n, c in count.items():  # Time: O(n)
            freq[c].append(n)
        
        # Step 3: Retrieve the top k most frequent numbers
        res = []
        for i in range(len(freq) - 1, 0, -1):  # Time: O(n + k)
            for n in freq[i]:  # Time: O(n)
                res.append(n)
                if len(res) == k:
                    return res
                
        """
        Time Complexity: O(n + k)
            - Counting frequencies: O(n)
            - Building freq list and retrieving top k elements: O(n + k)
        Space Complexity: O(n)
            - count dictionary: O(n)
            - freq list: O(n)
        """