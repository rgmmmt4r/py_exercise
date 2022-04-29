class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = set()
        while headA:
            A.add(headA)
            headA = headA.next
        while headB:
            if headB in A:
                return headB
            headB = headB.next
            