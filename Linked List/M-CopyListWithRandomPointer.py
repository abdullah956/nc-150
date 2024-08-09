class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        # Dictionary to store the mapping from the original nodes to their copies
        # Initialize with None mapping to None to handle the edge case of random pointers being None
        oldToCopy = {None: None}

        # First pass: Create copies of each node and store the mapping in the dictionary
        cur = head
        while cur:
            # Create a new node copy with the same value as the current node
            copy = Node(cur.val)
            # Map the original node to its copy
            oldToCopy[cur] = copy
            # Move to the next node in the original list
            cur = cur.next

        # Second pass: Assign the next and random pointers for each copied node
        cur = head
        while cur:
            # Get the copied node corresponding to the current node
            copy = oldToCopy[cur]
            # Set the next pointer of the copied node
            copy.next = oldToCopy[cur.next]
            # Set the random pointer of the copied node
            copy.random = oldToCopy[cur.random]
            # Move to the next node in the original list
            cur = cur.next

        # Return the head of the copied linked list, which corresponds to the head of the original list
        return oldToCopy[head]
