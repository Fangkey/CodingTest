from linked_list import ListNode, buildLinkedList, printLinkedList
from heapq import heappop, heappush

class Solution(object):
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

