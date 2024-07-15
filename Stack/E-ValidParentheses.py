from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        # Map to store the matching pairs of parentheses
        closeToOpen = {")": "(", "}": "{", "]": "["}
        stack = []  # Initialize an empty stack to keep track of opening parentheses

        for c in s:  # Iterate through each character in the input string
            if c in closeToOpen:  # If the character is a closing parenthesis
                if stack and stack[-1] == closeToOpen[c]:  # Check if the stack is not empty and the top of the stack matches the corresponding opening parenthesis
                    stack.pop()  # Pop the top of the stack since we found a matching pair
                else:
                    return False  # If no match is found, return False
            else:
                stack.append(c)  # If the character is an opening parenthesis, push it onto the stack

        return not stack  # Return True if the stack is empty, otherwise return False

# Time Complexity: O(n) - We iterate through each character in the string exactly once, 
# and each operation (push, pop, check) on the stack is O(1).

# Space Complexity: O(n) - In the worst case, the stack could contain all opening parentheses 
# which would be proportional to the input size.
