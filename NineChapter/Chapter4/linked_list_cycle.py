from linked_list import ListNode, buildLinkedList, printLinkedList

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        slow = head
        fast = head.next

        if fast is None:
            return False

        while fast is not None and fast.next is not None:
            if slow is fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2]
    head = buildLinkedList(nums)
    print s.hasCycle(head)

    nums = [0]
    head = buildLinkedList(nums)
    print s.hasCycle(head)

    nums = [1, 3, 5, 2, 4, 6]
    head = buildLinkedList(nums)
    head.next.next.next.next.next.next = head.next.next
    print s.hasCycle(head)

    nums = []
    head = buildLinkedList(nums)
    print s.hasCycle(head)

    nums = [0]
    head = buildLinkedList(nums)
    head.next = head
    print s.hasCycle(head)

