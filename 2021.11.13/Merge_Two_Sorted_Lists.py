# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None and l2 == None :
            return None
        elif l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None :
            return l1
        if l1.val <= l2.val:
            re_list = l1
        else:
            re_list = l2
        while(l1.next != None or l2.next != None):
            if l1.val <= l2.val:
                if l1.next.val:
                    if l1.next.val <= l2.val:
                        l1 = l1.next
                    else:
                        temp = l1.next
                        l1.next = l2
                        l1 = temp
                else:
                    l1.next = l2    
            else:
                if l2.next.val:
                    if l2.next.val < l1.val:
                        l2 = l2.next
                    else:
                        temp = l2.next
                        l2.next = l1
                        l2 = temp
                else:
                    l2.next = l1
        if l1.val <= l2.val:
            l1.next = l2         
        else:
            l2.next = l1
        return re_list




