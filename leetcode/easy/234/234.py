class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        this_list_val = []
        temp = head
        while temp:
            this_list_val.append(temp.val)
            temp = temp.next
        idx_backward = len(this_list_val) -1
        temp = head
        while temp:
            if temp.val != this_list_val[idx_backward]:
                return False
            temp = temp.next
            idx_backward -=1
        return True