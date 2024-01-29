class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def check(p, q):
            # If both nodes are None, they are equal
            if not p and not q:
                return True
            
            # If one of the nodes is None and the other is not, they are not equal
            if not p or not q:
                return False
            
            # If values are not equal, the trees are not the same
            if p.val != q.val:
                return False
            
            # Recursively check left and right subtrees
            return check(p.left, q.left) and check(p.right, q.right)
        
        return check(p, q)
