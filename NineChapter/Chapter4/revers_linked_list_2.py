from linked_list import ListNode, buildLinkedList, printLinkedList

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None

        if m == n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        start = dummy.next
        for i in range(0, m - 1):
            tail = start
            start = start.next

        if start.next is None:
            return dummy.next

        prev = None
        cur = start
        cnt = 0
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            cnt += 1
            if cnt >= n - m + 1:
                break

        tail.next = prev
        start.next = cur
        return dummy.next

if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 3]
    head = buildLinkedList(nums)
    head = s.reverseBetween(head, 1, 1)
    # [1, 2, 3]
    printLinkedList(head)

    nums = [1, 1, 2, 3, 3, 4, 5, 5]
    head = buildLinkedList(nums)
    head = s.reverseBetween(head, 3, 6)
    # [1, 1, 4, 3, 3, 2, 5, 5]
    printLinkedList(head)

    nums = [1, 1, 2, 3, 3, 4, 5, 5]
    head = buildLinkedList(nums)
    head = s.reverseBetween(head, 3, 8)
    # [1, 1, 5, 5, 4, 3, 3, 2]
    printLinkedList(head)

    nums = [1, 2]
    head = buildLinkedList(nums)
    head = s.reverseBetween(head, 2, 2)
    # [1, 2]
    printLinkedList(head)

    nums = [1, 2]
    head = buildLinkedList(nums)
    head = s.reverseBetween(head, 1, 2)
    # [2, 1]
    printLinkedList(head)

    nums = [1]
    head = buildLinkedList(nums)
    head = s.reverseBetween(head, 1, 1)
    # [1]
    printLinkedList(head)

    nums = []
    head = buildLinkedList(nums)
    head = s.reverseBetween(head, 0, 0)
    # []
    printLinkedList(head)