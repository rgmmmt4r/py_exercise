# wrong answer
from tkinter.tix import Tree
from trace import Trace


class Solution:
    def isSymmetric(self, root) -> bool:
        def symmetric_check(root1,root2):
            if root1 == None and  root2 == None:
                return True
            elif root1 !=None and root2 != None and root1.val == root2.val:
                return symmetric_check(root1.left,root2.right) and symmetric_check(root1.right,root2.left)
            return False
        return symmetric_check(root,root)

            

