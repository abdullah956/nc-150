class MinStack:
    def __init__(self):
        # Initialize two stacks:
        # - stack to store all the values
        # - minStack to store the minimum values
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Push the value onto the main stack
        self.stack.append(val)
        # Push the minimum value onto the minStack
        # The minimum value is either the current value or the last value in minStack
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # Remove the top element from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the minStack which is the minimum value
        return self.minStack[-1]

# Time Complexity:
# - push: O(1) - Each push operation involves appending to both stacks which is O(1) each.
# - pop: O(1) - Each pop operation involves removing the top element from both stacks which is O(1) each.
# - top: O(1) - Returning the top element of the main stack is O(1).
# - getMin: O(1) - Returning the top element of the minStack is O(1).

# Space Complexity: O(n) - In the worst case, we store all elements in both stacks.
# For each element in the main stack, we also store an element in the minStack. 
# Therefore, the space complexity is linear with respect to the number of elements pushed onto the stack.
