# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node
        dummy.next = head  # Point it to the head of the list
        cur = dummy
        while head:
            if head.val == val:
                cur.next = head.next
            else:
                cur = cur.next
            head = head.next
        return dummy.next