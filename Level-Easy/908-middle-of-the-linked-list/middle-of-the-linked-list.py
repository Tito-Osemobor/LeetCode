# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        templ = []
        while head != None:
            templ.append(head)
            head = head.next
        length = len(templ) 
        return templ[length // 2]
