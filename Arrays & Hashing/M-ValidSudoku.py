from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to keep track of seen numbers in columns, rows, and 3x3 squares
        cols = collections.defaultdict(set)    # Dictionary where each key is a column index, value is a set of seen numbers
        rows = collections.defaultdict(set)    # Dictionary where each key is a row index, value is a set of seen numbers
        squares = collections.defaultdict(set) # Dictionary where each key is a tuple (r//3, c//3), value is a set of seen numbers
        
        # Iterate through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":  # Skip empty cells
                    continue
                
                # Check if the number is already in the current row, column, or 3x3 square
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False  # If the number is found, the board is invalid
                
                # Add the number to the respective row, column, and 3x3 square sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True  # If no duplicates found, the board is valid

# Time Complexity: O(1)
# We always iterate through a fixed number of cells (81) in the 9x9 board.
# Each operation (checking and adding elements in sets) is O(1), thus the overall time complexity is O(1).

# Space Complexity: O(1)
# We use additional data structures (dictionaries of sets), but the size of these sets is limited to at most 9 elements each.
# The total number of elements stored is limited and does not scale with input size (fixed board size), so the space complexity is O(1).
