# coding=utf-8

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


# 2018-05-26 16:47
# 2018-05-26 16:56

from collections import deque

class Solution:
    # @param root, a tree link node
    # @return nothing
    
    def connect(self, root):
        dq = deque([])
        dq.append(root)
        
        levels = []
        while len(dq) != 0: 
            size = len(dq)
            cur_level = []
            for i in range(0, size):
                cur_node = dq.popleft()
                if cur_node is not None:
                    cur_level.append(cur_node)
                    dq.append(cur_node.left)
                    dq.append(cur_node.right)
        
            levels.append(cur_level)
            
        for l in levels:
            for i in range(0, len(l) - 1):
                cur_node = l[i]
                next_node = l[i + 1]
                cur_node.next = next_node