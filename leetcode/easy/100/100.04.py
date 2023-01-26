class Solution:
    result = True
    def isSameTree(self, p, q) -> bool:
        
        def inorder_at_the_same_time(p,q):
            if p and q:
                inorder_at_the_same_time(p.left,q.left)
                if p.val != q.val:
                    self.result = False
                inorder_at_the_same_time(p.right,q.right)
            elif p and not q:
                self.result = False
            elif not  p and q:
                self.result = False
        inorder_at_the_same_time(p,q)
        return self.result