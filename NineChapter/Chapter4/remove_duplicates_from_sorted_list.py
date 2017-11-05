from linked_list import ListNode, buildLinkedList, printLinkedList

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        cur = head
        while cur.next is not None:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == "__main__":
    s = Solution()

    nums = [1, 1, 2, 3, 3, 4, 5, 5]
    head = buildLinkedList(nums)
    head = s.deleteDuplicates(head)
    printLinkedList(head)

    nums = [1, 1]
    head = buildLinkedList(nums)
    head = s.deleteDuplicates(head)
    printLinkedList(head)

    nums = [1]
    head = buildLinkedList(nums)
    head = s.deleteDuplicates(head)
    printLinkedList(head)

    nums = []
    head = buildLinkedList(nums)
    head = s.deleteDuplicates(head)
    printLinkedList(head)
