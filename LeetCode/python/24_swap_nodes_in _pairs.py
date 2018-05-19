# coding=utf-8
# 2018-05-16:1:21
# 2018-05-16:1:30

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dumy = ListNode(0)
        dumy.next = head
        
        cur = dumy
        
        while cur is not None and cur.next is not None and cur.next.next is not None:
            next_first = cur.next.next.next
            cur_first = cur.next
            cur_second = cur.next.next
            cur.next = cur_second
            cur_second.next = cur_first
            cur_first.next = next_first
            cur = cur.next.next
            
        return dumy.next