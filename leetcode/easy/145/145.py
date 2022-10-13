class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        treeElement = []
        def postorderInput(root):
            if(root):
                postorderInput(root.left)
                postorderInput(root.right)
                treeElement.append(root.val)
        postorderInput(root)
        return treeElement