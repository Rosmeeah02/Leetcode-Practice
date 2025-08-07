# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next     # Save what's next
            curr.next = prev          # Reverse the pointer
            prev = curr               # Move prev forward
            curr = next_node          # Move curr forward

        return prev  # New head of the reversed list
