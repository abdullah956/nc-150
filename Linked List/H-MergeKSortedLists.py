# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # If the input list is empty or has no elements, return None
        if not lists or len(lists) == 0:
            return None

        # Continue merging until only one list remains
        while len(lists) > 1:
            mergedLists = []  # Temporary list to hold merged lists
            # Iterate through the list of linked lists in pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # Get the second list in the pair, if it exists
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                # Merge the two lists and append the result to mergedLists
                mergedLists.append(self.mergeList(l1, l2))
            # Update the lists to the newly merged lists
            lists = mergedLists
        # Return the fully merged list
        return lists[0]

    def mergeList(self, l1, l2):
        # Create a dummy node to help with list merging
        dummy = ListNode()
        tail = dummy  # Tail pointer for building the merged list

        # Merge the two lists until one of them is empty
        while l1 and l2:
            if l1.val < l2.val:
                # If l1's value is smaller, append it to the merged list
                tail.next = l1
                l1 = l1.next  # Move to the next node in l1
            else:
                # If l2's value is smaller or equal, append it to the merged list
                tail.next = l2
                l2 = l2.next  # Move to the next node in l2
            tail = tail.next  # Move the tail pointer forward

        # Append any remaining nodes from l1 or l2
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        # Return the merged list, which starts at dummy.next
        return dummy.next
