class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) :
        prev = None
        current = head
        while current:
            temp = current.next  # temporarily store the next node
            current.next = prev       # reverse the current node's pointer
            prev = current            # move prev and current one step forward
            current = temp
        return prev  # prev will be the new head at the end of the loop