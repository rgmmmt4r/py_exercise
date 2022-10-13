# pass
class Solution:
    flag = True
    def isSameTree(self, p, q) -> bool:
        def inOrder( p,q):
            cur1 = p
            cur2 = q
            if cur1 and cur2:
                inOrder(cur1.left,cur2.left)
                if cur1.val != cur2.val:
                    self.flag = False
                inOrder(cur1.right,cur2.right)
            elif cur1 == None and cur2:
                self.flag = False
            elif cur1 and cur2 == None:
                self.flag = False
        inOrder( p,q)
        return self.flag

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
p = TreeNode()
p.val = 1
p.left = 2

q = TreeNode()
q.val = 1
q.right = 2

s = Solution()
print(s.isSameTree(p,q))
