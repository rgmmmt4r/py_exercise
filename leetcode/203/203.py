class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        class ListNode:
            def __init__(self, val=0, next=None):
                self.val = val
                self.next = next
        temp = ListNode()
        root = temp
        temp.next = head
        while(temp.next != None):
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return root.next
