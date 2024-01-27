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
        
        

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Remove the 2nd node from the end
new_head = removeNthFromEnd(head, 2)

# Print the result: 1 -> 2 -> 3 -> 5
while new_head:
    print(new_head.val, end=" -> ")
    new_head = new_head.next
