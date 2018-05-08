from linked_list import ListNode, buildLinkedList, printLinkedList
from heapq import heappop, heappush

class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        h = []
        for i in range(0, k):
            if lists[i] is not None:
                heappush(h, (lists[i].val, lists[i]))

        dummy = ListNode(0)
        head = dummy
        while len(h) != 0:
            val, node = heappop(h)
            node_next = node.next
            head.next = node
            head = node
            if node_next is not None:
                heappush(h, (node_next.val, node_next))

        return dummy.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 2018-05-09 0:15
# 2018-05-09 0:30
from heapq import heapify, heappush, heappop

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        for i in range(0, len(lists)):
            n = lists[i]
            if n is not None:
                heappush(h, (n.val, n))

        d = ListNode(0)
        cur = d
        while len(h) != 0:
            val, n = heappop(h)
            cur.next = n
            cur = cur.next
            n = n.next
            if n is not None:
                heappush(h, (n.val, n))

        return d.next



if __name__ == "__main__":
    s = Solution()

    printLinkedList(s.mergeKLists([None, None]))

    nums = [1, 2, 4, 6, 8, 10]
    head1 = buildLinkedList(nums)

    nums = [1, 3, 5, 7, 9]
    head2 = buildLinkedList(nums)

    nums = [0]
    head3 = buildLinkedList(nums)

    printLinkedList(s.mergeKLists([head1, head2, head3]))

