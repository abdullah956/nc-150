class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy node to act as the head of the result list
        # 'current' will be used to build the new list
        head = ListNode()
        current = head
        
        # Initialize a variable to keep track of the carry value
        carry = 0
        
        # Loop until there are no more nodes in l1 or l2 and there is no carry left
        while l1 or l2 or carry:
            # Get the value of the current nodes in l1 and l2 (use 0 if the node is None)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate the sum of the two values plus any carry from the previous iteration
            val = v1 + v2 + carry
            
            # Update carry for the next iteration (carry is the tens place of the sum)
            carry = val // 10
            
            # Update the value to be stored in the current node (remainder after division by 10)
            val %= 10
            
            # Create a new node with the calculated value and add it to the result list
            current.next = ListNode(val)
            
            # Move the current pointer to the next node
            current = current.next
            
            # Move to the next nodes in l1 and l2, if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the head of the new list (skipping the dummy node)
        return head.next