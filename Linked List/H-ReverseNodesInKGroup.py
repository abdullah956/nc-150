class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0, head)
        groupPrev = dummy  # Pointer to the node before the current group

        while True:
            # Find the kth node from the current position
            kth = self.getKth(groupPrev, k)
            # If there are fewer than k nodes left, no more reversing is needed
            if not kth:
                break
            # Set the next group start node
            groupNext = kth.next

            # Reverse the nodes in the current group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next  # Temporarily store the next node
                curr.next = prev  # Reverse the current node
                prev = curr  # Move prev forward
                curr = tmp  # Move to the next node in the original list

            # Connect the reversed group back to the previous part of the list
            tmp = groupPrev.next  # Node at the start of the reversed group
            groupPrev.next = kth  # Connect the previous part to the end of the reversed group
            groupPrev = tmp  # Move groupPrev to the end of the reversed group

        # Return the new head of the list, which starts after the dummy node
        return dummy.next

    def getKth(self, curr, k):
        # Traverse the list to find the kth node from the current position
        while curr and k > 0:
            curr = curr.next
            k -= 1
        # Return the kth node, or None if there are fewer than k nodes remaining
        return curr
