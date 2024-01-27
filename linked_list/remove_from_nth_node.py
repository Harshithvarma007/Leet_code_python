# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        left,right=dummy,dummy

        for _ in range(n+1):
            right=right.next

        while right is not None:
            right=right.next
            left=left.next
        left.next=left.next.next
        return dummy.next
        
        
