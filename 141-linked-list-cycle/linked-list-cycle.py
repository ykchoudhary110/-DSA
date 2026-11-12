# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast is not None and fast.next is not None: # the fast check wheather its standing on none dn fast.next next check wheather next is not none specially in single elememnt linked list as we are moving 2 steps at a time
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        return False
        
        