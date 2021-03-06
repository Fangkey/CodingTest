from collections import deque

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution1:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        node_queue = deque([])
        node_queue.append(node)

        old_hashmap = dict()
        while len(node_queue) != 0:
            cur_node = node_queue.popleft()
            old_hashmap[cur_node.label] = cur_node
            for n in cur_node.neighbors:
                if n.label not in old_hashmap:
                    node_queue.append(n)

        new_hashmap = dict()
        for label, old_node in old_hashmap.items():
            new_node = UndirectedGraphNode(old_node.label)
            new_hashmap[label] = new_node

        for label, old_node in old_hashmap.items():
            new_node = new_hashmap[label]
            for n in old_node.neighbors:
                new_node.neighbors.append(new_hashmap[n.label])

        return new_hashmap[node.label]


# 2018-06-02 14:57
# 2018-06-02 15:03
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        dq = deque([])
        dq.append(node)

        old_to_new = dict()

        while len(dq) != 0:
            old = dq.popleft()
            if old not in old_to_new:
                new = UndirectedGraphNode(old.label)
                old_to_new[old] = new
                for nei in old.neighbors:
                    dq.append(nei)

        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])

        return old_to_new[node]



if __name__ == "__main__":
    s = Solution()

    n1 = UndirectedGraphNode(1)
    n2 = UndirectedGraphNode(2)
    n3 = UndirectedGraphNode(3)

    n1.neighbors.append(n2)
    n2.neighbors.append(n3)
    n3.neighbors.append(n1)

    new_node = s.cloneGraph(n1)
    print new_node