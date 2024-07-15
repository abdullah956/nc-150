from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Initialize an empty stack
        for c in tokens:
            if c == "+":
                # Pop the top two elements, add them, and push the result back onto the stack
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                # Pop the top two elements, subtract the second popped from the first popped, and push the result back onto the stack
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                # Pop the top two elements, multiply them, and push the result back onto the stack
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                # Pop the top two elements, divide the second popped by the first popped, convert to int, and push the result back onto the stack
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                # If the token is a number, convert it to an integer and push it onto the stack
                stack.append(int(c))
        return stack[0]  # The result is the only element left in the stack

# Time Complexity: O(n)
# We iterate through the tokens list once, performing a constant amount of work for each token (either pushing/popping from the stack or performing an arithmetic operation). Thus, the time complexity is linear in the number of tokens.

# Space Complexity: O(n)
# In the worst case, the stack can contain all the operands, which means the space complexity is linear in the number of tokens.
