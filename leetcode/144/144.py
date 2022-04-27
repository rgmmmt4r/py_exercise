class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree_elememt = []
        def inputElement(root):
            if root:
                tree_elememt.append(root.val)
                inputElement(root.left)
                inputElement(root.right)
        inputElement(root)
        return tree_elememt