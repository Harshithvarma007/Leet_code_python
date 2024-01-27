# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        # Find the middle of the list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        second_half = self.reverseList(slow.next)
        slow.next = None  # Cut off the first half

        # Merge the two halves
        self.mergeLists(head, second_half)
                                        
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

    def mergeLists(self, list1, list2):
        """
        Merges two linked lists in-place.
        """
        while list2:
            next_list1, next_list2 = list1.next, list2.next
            list1.next, list2.next = list2, next_list1
            list1, list2 = next_list1, next_list2
