class GraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        if len(prerequisites) == 0:
            return range(0, numCourses)

        # Generate Graph Nodes
        node_hash = dict()
        for cp in prerequisites:
            c = cp[0]
            p = cp[1]

            if c in node_hash:
                node_c = node_hash[c]
            else:
                node_c = GraphNode(c)
                node_hash[c] = node_c

            if p in node_hash:
                node_p = node_hash[p]
            else:
                node_p = GraphNode(p)
                node_hash[p] = node_p

            node_p.neighbors.append(node_c)

        # calc degree
        degree_hash = dict()
        for cp in prerequisites:
            c = cp[0]
            if c in degree_hash:
                degree_hash[c] = degree_hash[c] + 1
            else:
                degree_hash[c] = 1

        # find 0 degree node
        result = []
        for cp in prerequisites:
            p = cp[1]
            if p not in degree_hash:
                # important
                if not node_hash[p] in result:
                    result.append(node_hash[p])

        if len(result) == 0:
            return []

        start = 0
        while start < len(result):
            cur_node = result[start]
            start += 1
            for n in cur_node.neighbors:
                d_n = degree_hash[n.label]
                d_n = d_n - 1
                degree_hash[n.label] = d_n
                if d_n == 0:
                    result.append(n)

        if len(result) < len(node_hash):
            return []

        order = [n.label for n in result]
        for i in range(0, numCourses):
            if i not in order:
                order.append(i)

        return order


if __name__ == "__main__":
    s = Solution()
    print s.findOrder(3, [[1, 0], [2, 0]])
    # True
    print s.findOrder(2, [])
    # True
    print s.findOrder(1, [])
    # False
    print s.findOrder(4, [[1, 0], [2, 1], [3, 2], [1, 3]])
    # False
    print s.findOrder(5, [[1, 0], [2, 1], [3, 2], [1, 3], [1, 4]])
    # True
    print s.findOrder(4, [[1, 0], [2, 1], [1, 3]])
    # True
    print s.findOrder(6, [[1, 0], [2, 1], [1, 3]])
    # True
    print s.findOrder(2, [[1, 0]])
    # False
    print s.findOrder(2, [[1, 0], [0, 1]])
