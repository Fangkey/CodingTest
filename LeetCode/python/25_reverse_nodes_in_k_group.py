# coding=utf-8
# 2018-05-16 13:33
# 2018-05-16 14:33

from linked_list import ListNode, buildLinkedList, printLinkedList

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dumy = ListNode(0)
        dumy.next = head
        
        cur = dumy
        
        while cur is not None and cur.next is not None:
            sub_head = cur.next
            sub_tail = cur.next
            sub_len = 1
            for i in range(0, k - 1):
                sub_tail = sub_tail.next
                if sub_tail is None:
                    break
                sub_len += 1
            
            if sub_len == k:
                next_head = sub_tail.next
                new_head = self.revser_list(sub_head, k)
                sub_head.next = next_head
                cur.next = new_head
                cur = sub_head
            else:
                break
        return dumy.next
            
    def revser_list(self, sub_head, k):
        if k == 1:
            return sub_head
        
        cur = sub_head
        cur_next = cur.next
        for i in range(0, k - 1):
            cur_next_next = cur_next.next
            cur_next.next = cur
            cur = cur_next
            cur_next = cur_next_next      
        return cur        

if __name__ == "__main__":
    s = Solution()

    nums = [1,2,3,4,5]
    k = 2
    head = buildLinkedList(nums)
    result = s.reverseKGroup(head, k)
    printLinkedList(result)