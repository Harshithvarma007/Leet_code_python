# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        cur1 = l1
        cur2 = l2
        dummy = ListNode(0)
        current = dummy

        while cur1 and cur2:
            # Calculate the sum and carry for the current digits
            carry, add = divmod(cur1.val + cur2.val + carry, 10)

            # Move to the next nodes
            cur1, cur2 = cur1.next, cur2.next

            # Create a new node with the calculated sum
            current.next = ListNode(add)
            current = current.next

        # Handle any remaining digits in l1 or l2
        while cur1:
            carry, add = divmod(cur1.val + carry, 10)
            cur1 = cur1.next
            current.next = ListNode(add)
            current = current.next

        while cur2:
            carry, add = divmod(cur2.val + carry, 10)
            cur2 = cur2.next
            current.next = ListNode(add)
            current = current.next

        # If there's a remaining carry, create a new node for it
        if carry > 0:
            current.next = ListNode(carry)

        return dummy.next
