# wrong answer
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        listA = []
        listB = []
        def input_Val(input_list,head):
            if(head):
                input_list.append(head.val)
                input_Val(input_list,head.next)
        input_Val(listA,headA)
        input_Val(listB,headB)
        if(listA[len(listA)-1] == listB[len(listB)-1]):
            return None
        endSkip = 0
        while(listA[len(listA)-1-endSkip] == listB[len(listB)-1-endSkip]):
            endSkip +=1
        print(endSkip)
        
        

