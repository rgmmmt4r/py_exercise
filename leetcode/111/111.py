class Solution:
    def minDepth(self, root) -> int:
        if root == None:
            return 0
        elif root.left != None and  root.right != None :
            return min(self.minDepth(root.left),self.minDepth(root.right)) +1
        elif root.left == None and  root.right != None :
            return self.minDepth(root.right) + 1
        else:
            return self.minDepth(root.left) + 1