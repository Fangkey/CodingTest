from linked_list import ListNode, buildLinkedList, printLinkedList

class Solution1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        cur = dummy.next
        found = False
        while cur.next is not None:
            if not found:
                if cur.val == cur.next.val:
                    found = True
                    cur = cur.next
                else:
                    tail = tail.next
                    cur = cur.next
            else:
                if cur.val == cur.next.val:
                    cur = cur.next
                else:
                    tail.next = cur.next
                    cur = cur.next
                    found = False

        if found:
            tail.next = None

        return dummy.next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next is not None and cur.next.next is not None:
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next is not None and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next


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