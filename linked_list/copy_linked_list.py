# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # Pass 1: Make a copy of the original next to itself
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

        # Pass 2: Copy the random pointers
        cur = head
        while cur:
            dup = cur.next
            if cur.random:
                dup.random = cur.random.next
            cur = dup.next

        # Pass 3: Separate the original and the duplicate list
        new_head = head.next
        current = head
        while current:
            temp = current.next
            current.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            current = current.next
        return new_head
