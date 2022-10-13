#wrong answer
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inOrder( p: Optional[TreeNode],q: Optional[TreeNode]) ->bool:
            cur1 = p
            cur2 = q
            if cur1 and cur2:
                inOrder(cur1.left,cur2.left)
                if cur1.val != cur2.val:
                    return False
                inOrder(cur1.right,cur2.right)
            elif (cur1== None) and cur2:
                return  False
            elif cur1 and (cur2== None):
                return  False
        result = inOrder(p,q)
        if result == False:
            return result
        else:
            return True


