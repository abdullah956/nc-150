from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculate the maximum profit that can be achieved from buying and selling one stock.

        :param prices: List of stock prices.
        :return: Maximum profit.
        
        Time Complexity: O(n) where n is the length of prices.
        Space Complexity: O(1) since we only use a few variables.
        """
        res = 0  # Initialize the result (max profit) to 0.
        
        # Initialize the lowest price seen so far to the first price in the list.
        lowest = prices[0]
        
        # Iterate through each price in the list.
        for price in prices:
            # If the current price is lower than the lowest seen so far, update lowest.
            if price < lowest:
                lowest = price
            # Calculate the potential profit if we sold at the current price.
            # Update the result if this profit is higher than the previous max profit.
            res = max(res, price - lowest)
        
        return res  # Return the maximum profit.
