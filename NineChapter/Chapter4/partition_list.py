from linked_list import ListNode, buildLinkedList, printLinkedList

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None

        dummy_before = ListNode(0)
        cur_before = dummy_before
        dummy_after = ListNode(0)
        cur_after = dummy_after
        cur_head = head
        while cur_head is not None:
            if cur_head.val < x:
                cur_before.next = cur_head
                cur_before = cur_before.next
            else:
                cur_after.next = cur_head
                cur_after = cur_after.next
            cur_head = cur_head.next

        cur_before.next = dummy_after.next
        cur_after.next = None

        return dummy_before.next


if __name__ == "__main__":
    s = Solution()

    nums = [1, 3, 5, 2, 4, 6]
    head = buildLinkedList(nums)
    head = s.partition(head, 4.5)
    printLinkedList(head)

    nums = [1, 3, 5, 2, 4, 6]
    head = buildLinkedList(nums)
    head = s.partition(head, 0)
    printLinkedList(head)

    nums = [1, 3, 5, 2, 4, 6]
    head = buildLinkedList(nums)
    head = s.partition(head, 8)
    printLinkedList(head)