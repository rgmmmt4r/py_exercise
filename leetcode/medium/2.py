


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = str(l1.val)
        str2 = str(l2.val)
        while l1.next:
            str1 += str(l1.next.val)
            l1 = l1.next
        while l2.next:
            str2 += str(l2.next.val)
            l2 = l2.next
        num1 = 0 
        num2 = 0
        for i in range(len(str1)):
            num1 += (int(str1[len(str1)-1-i]) * (10**(len(str1)-1-i)))
        for j in range(len(str2)):
            num2 += (int(str2[len(str2)-1-j]) * (10**(len(str2)-1-j)))
        num = num1 + num2
        str_num = str(num)
        root = ListNode()
        temp = root
        for i in range(len(str_num)):
            temp.next = ListNode(int(str_num[len(str_num)-1-i]))
            temp = temp.next
        return root.next
