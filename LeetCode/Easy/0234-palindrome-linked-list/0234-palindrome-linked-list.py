# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        lis = []
        curr = head
        while curr:
            lis.append(curr.val)
            curr = curr.next
        
        n = len(lis)
        left = 0
        right = n-1
        
        while left < right:
            if lis[left] != lis[right]:
                return False
            left += 1
            right -= 1
        
        return True

        