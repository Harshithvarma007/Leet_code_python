# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur1 = list1
        cur2 = list2

        # Initialize an empty result list
        res = ListNode()
        current = res

        while cur1 is not None and cur2 is not None:
            if cur1.val <= cur2.val:
                current.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                current.next = ListNode(cur2.val)
                cur2 = cur2.next

            current = current.next

        # Append the remaining elements from list1 or list2
        if cur1 is not None:
            current.next = cur1
        elif cur2 is not None:
            current.next = cur2

        # The head of the merged list is the next node of the initial dummy node
        return res.next
