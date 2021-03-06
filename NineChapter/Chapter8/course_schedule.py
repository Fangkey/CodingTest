class GraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # important
        if len(prerequisites) == 0:
            return True

        node_hashmap = dict()

        for cp in prerequisites:
            c = cp[0]
            p = cp[1]
            if p in node_hashmap:
                node_p = node_hashmap[p]
            else:
                node_p = GraphNode(p)
                node_hashmap[p] = node_p

            if c in node_hashmap:
                node_c = node_hashmap[c]
            else:
                node_c = GraphNode(c)
                node_hashmap[c] = node_c
            node_p.neighbors.append(node_c)

        degree_map = dict()
        for cp in prerequisites:
            c = cp[0]
            if c in degree_map:
                degree_map[c] = degree_map[c] + 1
            else:
                degree_map[c] = 1

        node_queue = []
        for cp in prerequisites:
            p = cp[1]
            if p not in degree_map:
                node_queue.append(node_hashmap[p])

        if len(node_queue) == 0:
            return False

        visited_hashmap = dict()
        start = 0
        while start < len(node_queue):
            cur_node = node_queue[start]
            visited_hashmap[cur_node.label] = cur_node
            start += 1
            for n in cur_node.neighbors:
                d_n = degree_map[n.label]
                d_n -= 1
                degree_map[n.label] = d_n
                if d_n == 0:
                    node_queue.append(n)
                    if n.label in visited_hashmap:
                        return False

        # important
        if len(visited_hashmap) != len(node_hashmap):
            return False

        return True

# 2018-06-02 16:35
# 2018-06-02 17:04

from collections import defaultdict, deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pre_cnt = defaultdict(int)
        neighbors = defaultdict(list)

        for cur, pre in prerequisites:
            pre_cnt[cur] += 1
            neighbors[pre].append(cur)

        start_set = set()
        for cur, pre in prerequisites:
            if pre not in pre_cnt:
                start_set.add(pre)

        dq = deque(list(start_set))
        while dq:
            cur = dq.popleft()
            for nei in neighbors[cur]:
                pre_cnt[nei] -= 1
                if pre_cnt[nei] == 0:
                    dq.append(nei)

        for p, cnt in pre_cnt.items():
            if cnt > 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    # False
    print s.canFinish(4, [[1, 0], [2, 1], [3, 2], [1, 3]])
    # True
    print s.canFinish(3, [[1,0],[2,1]])
    # True
    print s.canFinish(3, [[1, 0], [2, 0]])
    # True
    print s.canFinish(2, [])
    # True
    print s.canFinish(1, [])
    # False
    print s.canFinish(5, [[1, 0], [2, 1], [3, 2], [1, 3], [1, 4]])
    # True
    print s.canFinish(4, [[1, 0], [2, 1], [1, 3]])
    # True
    print s.canFinish(2, [[1, 0]])
    # False
    print s.canFinish(2, [[1, 0], [0, 1]])


