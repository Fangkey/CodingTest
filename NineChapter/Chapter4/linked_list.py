# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def buildLinkedList(nums):
    if len(nums) == 0:
        return None

    head = ListNode(nums[0])
    cur = head
    for n in nums[1: ]:
        node = ListNode(n)
        cur.next = node
        cur = node

    return head


def printLinkedList(head):
    result = []
    while head is not None:
        result.append(head.val)
        head = head.next
    print result