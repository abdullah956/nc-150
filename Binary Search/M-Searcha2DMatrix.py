from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time Complexity: O(log m + log n), where m is the number of rows and n is the number of columns
        # Space Complexity: O(1), since we are using only a constant amount of extra space
        
        # Get the number of rows and columns
        ROWS, COLS = len(matrix), len(matrix[0])

        # Initialize pointers for the binary search on rows
        top, bot = 0, ROWS - 1
        
        # Perform binary search to find the correct row
        while top <= bot:
            row = (top + bot) // 2
            # If the target is greater than the last element of the current row, move the top pointer down
            if target > matrix[row][-1]:
                top = row + 1
            # If the target is less than the first element of the current row, move the bottom pointer up
            elif target < matrix[row][0]:
                bot = row - 1
            # If the target is within the range of the current row, break out of the loop
            else:
                break

        # If no valid row is found, return False
        if not (top <= bot):
            return False
        
        # The row in which the target might exist
        row = (top + bot) // 2
        
        # Initialize pointers for the binary search on columns within the identified row
        l, r = 0, COLS - 1
        
        # Perform binary search to find the target within the row
        while l <= r:
            m = (l + r) // 2
            # If the target is greater than the mid element, adjust the left pointer
            if target > matrix[row][m]:
                l = m + 1
            # If the target is less than the mid element, adjust the right pointer
            elif target < matrix[row][m]:
                r = m - 1
            # If the target is found, return True
            else:
                return True
        
        # If the target is not found, return False
        return False
