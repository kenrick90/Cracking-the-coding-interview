#https://leetcode.com/problems/partition-list/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        firstBelowPointer = None
        lastBelowPointer = None
        firstAbovePointer = None
        lastAbovePointer = None
        
        Pointer = head
        
        while Pointer is not None:
            if Pointer.val < x:
                if firstBelowPointer is not None:
                    lastBelowPointer.next = Pointer
                    lastBelowPointer = Pointer
                else:
                    firstBelowPointer = Pointer
                    lastBelowPointer  = Pointer
            if Pointer.val >= x:
                if firstAbovePointer is None:
                    firstAbovePointer = Pointer
                    lastAbovePointer = Pointer
                else:
                    lastAbovePointer.next = Pointer
                    lastAbovePointer = Pointer
            
            Pointer = Pointer.next
        
        if lastAbovePointer is None:
            return firstBelowPointer
        else:
            lastAbovePointer.next = None
        
        if lastBelowPointer is not None:
            lastBelowPointer.next = firstAbovePointer
            return firstBelowPointer
        else:
            return firstAbovePointer
        
