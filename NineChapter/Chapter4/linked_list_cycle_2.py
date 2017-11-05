from linked_list import ListNode, buildLinkedList, printLinkedList


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None

        slow = head
        fast = head.next

        found = False
        while fast is not None and fast.next is not None:
            if slow is fast:
                found = True
                break

            slow = slow.next
            fast = fast.next.next

        if not found:
            return None

        # critical
        while head is not slow.next:
            head = head.next
            slow = slow.next

        return head


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2]
    head = buildLinkedList(nums)
    print s.detectCycle(head)


    nums = [0]
    head = buildLinkedList(nums)
    print s.detectCycle(head)

    nums = [1, 3, 5, 2, 4, 6]
    head = buildLinkedList(nums)
    head.next.next.next.next.next.next = head.next.next
    print s.detectCycle(head)

    nums = []
    head = buildLinkedList(nums)
    print s.detectCycle(head)

    nums = [0]
    head = buildLinkedList(nums)
    head.next = head
    print s.detectCycle(head)