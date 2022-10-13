from numpy import true_divide


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            if slow.next == fast.next.next:
                return True
            slow = slow.next
            fast = fast.next.next
        return False