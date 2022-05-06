
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
        list_val = []
        
        while(head):
            list_val.append(head.val)
            head = head.next
        if len(list_val) == 0:
            return None
        root2 = ListNode()
        temp = ListNode(list_val.pop())
        root2.next = temp
        for i in range(len(list_val)-1,-1,-1):
            temp.next = ListNode(list_val.pop())
            temp = temp.next
        return root2.next


