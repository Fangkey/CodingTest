# coding=utf-8

# 2018-05-11 12:43
# 2018-05-11 12:46

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        cur = head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
            
        if l1 is not None:
            cur.next = l1
        if l2 is not None:
            cur.next = l2
            
        return head.next