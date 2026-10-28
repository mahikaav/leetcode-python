# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow 
        prev = None

        while curr:
            next_ = curr.next 
            curr.next = prev
            prev = curr
            curr = next_
        
        first = head
        second = prev

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        

        