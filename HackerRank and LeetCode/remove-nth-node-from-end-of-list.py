#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        frontPointer, endPointer= head,head
        
        for i in range(n):
            endPointer = endPointer.next
            
        if endPointer != None:
            while endPointer.next != None:
                frontPointer = frontPointer.next
                endPointer = endPointer.next
            frontPointer.next=frontPointer.next.next
            return head
        
        if endPointer == None:
            head=head.next
            return head
