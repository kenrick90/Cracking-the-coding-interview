#https://leetcode.com/problems/rotate-list/submissions/
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arrayOfLL =[ None for _ in range(200001)]
        runner = head
        while runner is not None:
            prev = runner
            runner = runner.next
            prev.next = arrayOfLL[prev.val +100000]
            arrayOfLL[prev.val +100000] = prev
        
        head = None
        for val in range(200000,-1,-1):
            if arrayOfLL[val] is not None:
                runner = arrayOfLL[val]
                while runner.next is not None:
                    runner = runner.next
                runner.next = head
                head = arrayOfLL[val]
        return head
        
