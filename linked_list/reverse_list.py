# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        cur = head.next
        prev = head
        ahead = cur.next

        while ahead is not None:
            cur.next = prev
            prev = cur
            cur = ahead
            ahead = cur.next

        # Update the last node to become the new head
        cur.next = prev

        # The original head should now point to None
        head.next = None

        return cur
        