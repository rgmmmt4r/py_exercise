class Solution:
    def isSymmetric(self, root) -> bool:
        def inorder(p,q):
            if p and q:
                if p.val != q.val:
                    return False
                return inorder(p.left,q.right) and      inorder(p.right,q.left)
            elif not p and q:
                return False
            elif p and not q:
                return False
            return True
        if root:
            return inorder(root.left,root.right)  
        else:
            return True