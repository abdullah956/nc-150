class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to act as the start of the merged list
        dummy = ListNode()
        # Initialize the current pointer to point to the dummy node
        current = dummy
        
        # Loop until either list1 or list2 is exhausted
        while list1 and list2:
            # Compare the current values of list1 and list2
            if list1.val < list2.val:
                # If list1's value is smaller, append it to the merged list
                current.next = list1
                # Move list1's pointer to the next node
                list1 = list1.next
            else:
                # If list2's value is smaller or equal, append it to the merged list
                current.next = list2
                # Move list2's pointer to the next node
                list2 = list2.next
            # Move the current pointer to the next node in the merged list
            current = current.next
        
        # If list1 still has nodes left, append the remainder to the merged list
        if list1:
            current.next = list1
        else:
            # If list2 still has nodes left, append the remainder to the merged list
            current.next = list2
        
        # Return the next node of dummy, which is the head of the merged list
        return dummy.next
