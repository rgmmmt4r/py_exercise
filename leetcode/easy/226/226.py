
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root == None:
            return None
        temp = root
        self.invert(root)
        self.invertTree(root.left)
        self.invertTree(root.right)
        
            
        
        return temp
    
    def invert(self,root):
        temp = root.left
        root.left = root.right
        root.right = temp
        return root


S = Solution()
print()