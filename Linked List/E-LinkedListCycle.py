class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize two pointers, slow and fast, both starting at the head of the list
        slow, fast = head, head

        # Traverse the list with two pointers
        while fast and fast.next:
            # Move the slow pointer by one step
            slow = slow.next
            # Move the fast pointer by two steps
            fast = fast.next.next

            # If the slow pointer and fast pointer meet, it means there is a cycle
            if slow == fast:
                return True
        
        # If we exit the loop, it means there is no cycle in the list
        return False
