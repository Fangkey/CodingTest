from linked_list import ListNode, buildLinkedList, printLinkedList

class Solution(object):
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        if head is None:
            return None
        cur = head
        cur_next = head.next
        head.next = None

        while cur_next is not None:
            cur_next_next = cur_next.next
            cur_next.next = cur
            cur = cur_next
            cur_next = cur_next_next

        return cur

    def mergeList(self, head1, head2):
        dummy = ListNode(0)
        cur_head = dummy
        while head1 is not None and head2 is not None:
            cur_head.next = head1
            head1 = head1.next
            cur_head.next.next = head2
            head2 = head2.next
            cur_head = cur_head.next.next

        if head1 is not None:
            cur_head.next = head1
        if head2 is not None:
            cur_head.next = head2

        return dummy.next

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        mid = self.findMid(head)
        head2 = self.reverseList(mid.next)
        mid.next = None
        self.mergeList(head, head2)

if __name__ == "__main__":
    s = Solution()

    nums = [1, 3, 5, 2, 4, 6]
    head = buildLinkedList(nums)
    head = s.reorderList(head)
    printLinkedList(head)

    nums = []
    head = buildLinkedList(nums)
    head = s.reorderList(head)
    printLinkedList(head)

    nums = [0]
    head = buildLinkedList(nums)
    head = s.reorderList(head)
    printLinkedList(head)