class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution1(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        cur_head = head
        while cur_head is not None:
            new_cur = RandomListNode(cur_head.label)
            cur_next = cur_head.next
            cur_head.next = new_cur
            new_cur.next = cur_next
            cur_head = cur_next

        cur_head = head
        cur_new_head = head.next
        while cur_head is not None:
            cur_rand = cur_head.random
            if cur_rand is not None:
                cur_new_head.random = cur_rand.next
            cur_head = cur_head.next.next
            if cur_head is not None:
                cur_new_head = cur_head.next

        new_head = head.next
        cur_head = head
        cur_new_head = head.next
        while cur_head is not None:
            cur_head_next = cur_head.next.next
            if cur_head_next is not None:
                cur_new_head.next = cur_head_next.next
                cur_new_head = cur_new_head.next

            cur_head.next = cur_head_next
            cur_head = cur_head.next

        return new_head


def printRandomList(head):
    result = []
    while head is not None:
        val = head.label
        if head.random is None:
            ran = None
        else:
            ran = head.random.label
        result.append((val, ran))
        head = head.next

    print result


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

# 2018-05-08 23:32
# 2018-05-08 23:57

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None

        cur = head
        while cur is not None:
            new_node = RandomListNode(cur.label)
            cur_next = cur.next
            cur.next = new_node
            cur.next.next = cur_next
            cur = cur.next.next

        cur = head
        while cur is not None :
            new_node = cur.next
            if cur.random is None:
                new_node.random = None
            else:
                new_node.random = cur.random.next
            cur = cur.next.next

        cur = head
        new_head = cur.next
        cur_new = cur.next
        while cur is not None:
            cur.next = cur_new.next
            if cur.next is not None:
                next_new = cur.next.next
                cur_new.next = next_new
                cur_new = next_new
            cur = cur.next

        return new_head





if __name__ == "__main__":
    s = Solution()

    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node4 = RandomListNode(4)
    node5 = RandomListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node2.random = node1
    node3.random = node5
    node4.random = node5
    node5.random = node1

    printRandomList(node1)
    head = s.copyRandomList(node1)
    printRandomList(head)


    printRandomList(None)
    head = s.copyRandomList(None)
    printRandomList(head)




