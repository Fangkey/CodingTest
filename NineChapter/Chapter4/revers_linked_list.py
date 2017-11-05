from linked_list import ListNode, buildLinkedList, printLinkedList

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = None
        cur_next = head
        while cur_next is not None:
            cur_next_next = cur_next.next
            cur_next.next = cur
            cur = cur_next
            cur_next = cur_next_next

        return cur

if __name__ == "__main__":
    s = Solution()

    nums = [1, 1, 2, 3, 3, 4, 5, 5]
    head = buildLinkedList(nums)
    head = s.reverseList(head)
    printLinkedList(head)

    nums = [1, 2]
    head = buildLinkedList(nums)
    head = s.reverseList(head)
    printLinkedList(head)

    nums = [1]
    head = buildLinkedList(nums)
    head = s.reverseList(head)
    printLinkedList(head)

    nums = []
    head = buildLinkedList(nums)
    head = s.reverseList(head)
    printLinkedList(head)