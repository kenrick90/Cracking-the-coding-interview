#https://github.com/kenrick90/Cracking-the-coding-interview/new/main/HackerRank%20and%20LeetCode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        counter = 0
        pointer = head
        while pointer != None:
            pointer = pointer.next
            counter += 1
        
        k = k % counter
        while k > 0:
            originalHead = head
            pointer = head
            while pointer.next is not None:
                if pointer.next.next is None:
                    secondlast = pointer
                pointer = pointer.next

            #pointer should now be poiting to last node
            head = pointer
            head.next = originalHead
            secondlast.next = None
            k -= 1
        return head
        
