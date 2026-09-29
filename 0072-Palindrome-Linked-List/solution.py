# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        slow = head
        fast = head

        # Find the middle of the linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        previous = None

        while slow:
            next_node = slow.next
            slow.next = previous
            previous = slow
            slow = next_node

        # Compare first half with reversed second half
        left = head
        right = previous

        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True