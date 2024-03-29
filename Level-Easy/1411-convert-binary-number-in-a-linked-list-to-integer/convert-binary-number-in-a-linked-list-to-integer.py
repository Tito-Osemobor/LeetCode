# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = ''
        while head is not None:
            answer += str(head.val)
            head = head.next
        return int(answer, 2)