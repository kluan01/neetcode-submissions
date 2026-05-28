class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        # move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # move both until fast is at last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow.next is the node to remove
        slow.next = slow.next.next
        return dummy.next
