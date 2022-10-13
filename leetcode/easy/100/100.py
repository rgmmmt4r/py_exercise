#wrong answer
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_list = []
        q_list = []
        def p_list_input_val(root: Optional[TreeNode]):
            cur = root
            if cur:
                p_list_input_val(cur.left)
                p_list.append(cur.val)
                p_list_input_val(cur.right)
            else:
                p_list.append('null')
        def q_list_input_val(root: Optional[TreeNode]):
            cur = root
            if cur:
                q_list_input_val(cur.left)
                q_list.append(cur.val)
                q_list_input_val(cur.right)
            else:
                q_list.append('null')
        p_list_input_val(p)
        q_list_input_val(q)
        if len(p_list) != len(q_list):
            return False
        for i in range(len(p_list)):
            if p_list[i] != q_list[i]:
                return False
        return True

