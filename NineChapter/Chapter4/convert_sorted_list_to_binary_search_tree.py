import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from linked_list import ListNode, buildLinkedList, printLinkedList
from Chapter3.binary_search_tree import BinarySearchTree, TreeNode, build_tree


class Solution1(object):
    def findMid(self, head, tail):
        slow = head
        fast = head.next

        while fast is not tail and fast.next is not tail:
            slow = slow.next
            fast = fast.next.next

        return slow

    def helper(self, head, tail):
        if head.next is tail:
            if head is None:
                return None
            else:
                return TreeNode(head.val)

        mid = self.findMid(head, tail)
        root = TreeNode(mid.val)
        if mid is not head:
            left_root = self.helper(head, mid)
        else:
            left_root = None

        right_root = self.helper(mid.next, tail)

        root.left = left_root
        root.right = right_root

        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        return self.helper(head, None)


class Solution2(object):
    current = None

    def helper(self, size):
        if size <= 0:
            return None

        left = self.helper(size / 2)
        root = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.helper(size - 1 - size / 2)
        root.left = left
        root.right = right

        return root

    def get_length(self, head):
        size = 0
        while head is not None:
            head = head.next
            size += 1
        return size

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None
        size = self.get_length(head)
        self.current = head
        return self.helper(size)



# 2018-08-08 23:12
# 2018-08-08 23:30

class Solution(object):

    current = None

    def helper(self, size):
        if size == 0:
            return None

        left = self.helper(size / 2)
        root = TreeNode(self.current.val)
        self.current = self.current.next
        right = self.helper(size - 1 - size / 2)
        root.left = left
        root.right = right
        return root

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.current = head
        size = 0
        while self.current is not None:
            self.current = self.current.next
            size += 1

        self.current = head
        return self.helper(size)


if __name__ == '__main__' and __package__ is None:
    s = Solution()
    # balanced BST cannot has two same node
    nums = [0, 1, 2, 3, 4, 5, 6, 7]
    head = buildLinkedList(nums)
    root = s.sortedListToBST(head)

    print root