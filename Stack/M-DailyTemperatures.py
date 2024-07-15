from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the result list with zeros, the same length as temperatures
        res = [0] * len(temperatures)
        # Initialize an empty stack to keep track of pairs [temperature, index]
        stack = []  # pair: [temp, index]

        # Iterate through each temperature with its index
        for i, t in enumerate(temperatures):
            # While the stack is not empty and the current temperature is greater than the temperature at the top of the stack
            while stack and t > stack[-1][0]:
                # Pop the top element from the stack
                stackT, stackInd = stack.pop()
                # Calculate the number of days to wait for a warmer temperature
                res[stackInd] = i - stackInd
            # Append the current temperature and its index to the stack
            stack.append((t, i))
        # Return the result list
        return res

# Time Complexity: O(n), where n is the length of temperatures. Each temperature is processed in constant time,
# and each index is pushed and popped from the stack at most once.

# Space Complexity: O(n), where n is the length of temperatures. This is due to the storage used by the result list
# and the stack, which can grow up to the size of temperatures in the worst case (e.g., temperatures in descending order).
