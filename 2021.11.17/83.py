#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        if head.next == None:
            return head
        start = ListNode()
        start.next = head
        second = head
        while True:
            while second.next.val == second.val:
                second = second.next
                if second.next == None:
                    head.next = None
                    return start.next
                elif second.next.val > second.val:
                    second = second.next
                    head.next = second
                    head = second
                    if second.next == None:
                        return start.next
            while second.next.val > second.val:
                second = second.next
                head = second
                if second.next == None:
                    return start.next
                elif second.next.val == second.val:
                    second = second.next
                    if second.next == None:
                        head.next = None
                        return start.next
                    else:
                        head.next = second.next
'''
h5 = ListNode()
h5.val = 3
h5.next = None

'''


h4 = ListNode()
h4.val = 3
h4.next = None

h3 = ListNode()
h3.val = 2
h3.next = h4

h2 = ListNode()
h2.val = 2
h2.next = h3





h1 = ListNode()
h1.val = 1
h1.next = h2



s = Solution()
a = s.deleteDuplicates(h1)
print(a)


        