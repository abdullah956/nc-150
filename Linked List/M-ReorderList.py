class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def reorderList(self, head: ListNode) -> None:
        # Step 1: Find the middle of the linked list
        slow, fast = head, head.next
        # Use two pointers: slow moves one step at a time, fast moves two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        # 'second' will point to the first node of the second half
        second = slow.next
        # Break the link between the first and second halves
        prev = slow.next = None
        # Reverse the second half of the list
        while second:
            tmp = second.next   # temporarily store the next node
            second.next = prev  # reverse the current node's pointer
            prev = second       # move 'prev' to the current node
            second = tmp        # move 'second' to the next node in the original order

        # Step 3: Merge the two halves of the list
        first, second = head, prev  # 'first' is the start of the first half, 'second' is the start of the reversed second half
        while second:
            # Temporarily store the next nodes of 'first' and 'second'
            tmp1, tmp2 = first.next, second.next
            # Link the current node of the first half to the current node of the second half
            first.next = second
            # Link the current node of the second half to the next node of the first half
            second.next = tmp1
            # Move 'first' and 'second' to their respective next nodes
            first, second = tmp1, tmp2
