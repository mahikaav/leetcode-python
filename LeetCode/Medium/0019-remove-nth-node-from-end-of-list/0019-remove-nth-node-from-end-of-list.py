# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0  
        curr = head

        while curr:
            length += 1
            curr = curr.next

        if length == n:
            return head.next
        
        stop = length - n - 1


        curr = head
        for _ in range(stop):
            curr = curr.next

        curr.next = curr.next.next
        return head
        