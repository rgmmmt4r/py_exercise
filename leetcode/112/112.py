class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        def checkSum(node,targetSum,curSum = 0) -> bool:
            curSum += node.val
            if curSum == targetSum and not node.left and not node.right:
                return True
            
            else:
                left = right = False
                if node.left:
                    left = checkSum(node.left,targetSum,curSum)
                if node.right:
                    right = checkSum(node.right,targetSum,curSum)
                return left or right
        return root and checkSum(root,targetSum)