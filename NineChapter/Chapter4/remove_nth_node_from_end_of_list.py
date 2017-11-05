from linked_list import ListNode, buildLinkedList, printLinkedList

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        for i in range(0, n):
            fast = fast.next

        slow = dummy
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()

    nums = [1]
    head = buildLinkedList(nums)
    root = s.removeNthFromEnd(head, 1)
    printLinkedList(root)

    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    head = buildLinkedList(nums)
    root = s.removeNthFromEnd(head, 2)
    printLinkedList(root)