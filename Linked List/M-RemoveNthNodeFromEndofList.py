class ListNode:
    def __init__(self, val=0, next=None):
        # Initialize the node with a value and a pointer to the next node
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node that points to the head of the list
        # This helps handle edge cases, such as removing the first node
        dummy = ListNode(0, head)
        
        # Initialize two pointers, left starting at the dummy node
        # and right starting at the head of the list
        left = dummy
        right = head
        
        # Move the right pointer `n` steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # Move both pointers until right reaches the end of the list
        # Left pointer will then point to the node before the one to be removed
        while right:
            left = left.next
            right = right.next
        
        # Skip the node to be removed by changing the `next` pointer
        left.next = left.next.next
        
        # Return the new head of the list, which is the next node of the dummy node
        return dummy.next
