from linked_list import ListNode, buildLinkedList, printLinkedList

class Solution(object):
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeList(self, head1, head2):
        dummy = ListNode(0)
        head = dummy
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                head.next = head1
                head1 = head1.next
                head = head.next
            else:
                head.next = head2
                head2 = head2.next
                head = head.next

        if head1 is not None:
            head.next = head1

        if head2 is not None:
            head.next = head2

        return dummy.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        mid = self.findMid(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)

        return self.mergeList(left, right)

if __name__ == "__main__":
    s = Solution()

    nums = [1, 3, 5, 2, 4, 6]
    head = buildLinkedList(nums)
    head = s.sortList(head)
    printLinkedList(head)

    nums = []
    head = buildLinkedList(nums)
    head = s.sortList(head)
    printLinkedList(head)

    nums = [0]
    head = buildLinkedList(nums)
    head = s.sortList(head)
    printLinkedList(head)