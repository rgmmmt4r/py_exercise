# wrong answer
from tkinter.tix import Tree
from trace import Trace


class Solution:
    left_stack = []
    right_stack = []
    def isSymmetric(self, root) -> bool:
        self.left_stack = []
        self.right_stack = []
        if root.left!= None and root.right!= None:
            def inoder_left(root1):
                cur = root1
                if cur != None:
                    inoder_left(cur.left)
                    self.left_stack.append(cur.val)
                    inoder_left(cur.right)
                else:
                    self.left_stack.append("None")
            inoder_left(root.left)
            def inoder_right(root2):
                cur = root2
                if cur!= None:
                    inoder_right(cur.right)
                    self.right_stack.append(cur.val)
                    inoder_right(cur.left)
                else:
                    self.right_stack.append("None")
            inoder_right(root.right)
            if len(self.left_stack) != len(self.right_stack):
                return False
            for i in range(len(self.left_stack)):
                if self.left_stack[i] != self.right_stack[i]:
                    return False
            return True
        elif (root.left == None and root.right != None) or (root.left != None and root.right == None):
            return False
        else:
            return True
            
            
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node_left = TreeNode(2)
node_right = TreeNode(2)
root = TreeNode(1,node_left,node_right)
s = Solution()
print(s.isSymmetric(root))

