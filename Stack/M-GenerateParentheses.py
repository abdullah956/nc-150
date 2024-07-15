from typing import List

#only add open paranthesis if open < n
#only add closed paranthesis if closed < open
#valid if open=closed=n
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []  # Stack to keep track of the current sequence of parentheses
        res = []    # Result list to store all valid combinations

        def backtrack(openN, closedN):
            # Base case: if the number of open and closed parentheses both equal to n
            if openN == closedN == n:
                res.append("".join(stack))  # Append the current sequence to the result list
                return

            # If the number of open parentheses is less than n, add an open parenthesis
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)  # Recurse with one more open parenthesis
                stack.pop()  # Backtrack: remove the last added parenthesis

            # If the number of closed parentheses is less than the number of open ones, add a closed parenthesis
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)  # Recurse with one more closed parenthesis
                stack.pop()  # Backtrack: remove the last added parenthesis

        backtrack(0, 0)  # Start the recursion with 0 open and 0 closed parentheses
        return res

# Time Complexity: O(4^n / √n)
# There are Catalan number C(n) valid sequences, which is asymptotically equivalent to 4^n / (n√n).
# Each valid sequence requires O(n) time to build.

# Space Complexity: O(n)
# The space used by the stack and the recursion stack is proportional to the depth of the recursion, which is O(n).
