from heapq import heappush, heapify

class Solution(object):
    def checkLeft(self, key_points):
        temp = []
        last_pt = key_points[-1]
        while len(key_points) > 0 and key_points[-1][0] == last_pt[0]:
            temp.append(key_points[-1])
            key_points.pop()

        max_pt = max(temp, key=lambda d: d[1])
        key_points.append(max_pt)

    def checkRight(self, key_points):
        temp = []
        last_pt = key_points[-1]
        while len(key_points) > 0 and key_points[-1][0] == last_pt[0]:
            temp.append(key_points[-1])
            key_points.pop()

        min_pt = min(temp, key=lambda d: d[1])
        key_points.append(min_pt)

    def checkSame(self, key_points):
        temp = []
        last_pt = key_points[-1]
        while len(key_points) > 0 and key_points[-1][1] == last_pt[1]:
            temp.append(key_points[-1])
            key_points.pop()

        min_pt = min(temp, key=lambda d: d[0])
        key_points.append(min_pt)


    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        border_list = []
        for b in buildings:
            border_list.append([b[0], b[2], 0])
            border_list.append([b[1], b[2], 1])

        sorted_border_list = sorted(border_list, key=lambda b: b[0])

        height_heap = []
        key_points = []
        for b in sorted_border_list:
            if b[2] == 0:
                if len(height_heap) == 0:
                    key_points.append([b[0], b[1]])
                    self.checkLeft(key_points)
                    self.checkSame(key_points)
                else:
                    max_height = -height_heap[0]
                    if b[1] > max_height:
                        key_points.append([b[0], b[1]])
                        self.checkLeft(key_points)
                        self.checkSame(key_points)
                heappush(height_heap, -b[1])
            else:
                height_heap.remove(-b[1])
                if len(height_heap) == 0:
                    key_points.append([b[0], 0])
                    self.checkRight(key_points)
                    self.checkSame(key_points)
                else:
                    heapify(height_heap)
                    max_height = -height_heap[0]
                    if b[1] > max_height:
                        key_points.append([b[0], max_height])
                        self.checkRight(key_points)
                        self.checkSame(key_points)

        return key_points


if __name__ == "__main__":
    buildings = [
        [4, 10, 10],
        [5, 10, 9],
        [6, 10, 8],
        [7, 10, 7],
        [8, 10, 6],
        [9, 10, 5]
    ]
    s = Solution()
    # [[4, 10], [10, 0]]
    print s.getSkyline(buildings)

    buildings = [
        [2, 4, 7],
        [2, 4, 5],
        [2, 4, 6]
    ]
    s = Solution()
    # [[2, 7], [4, 0]]
    print s.getSkyline(buildings)

    buildings = [
        [2, 9, 10],
        [9, 12, 15]
    ]
    s = Solution()
    # [[2,10],[9,15],[12,0]]
    print s.getSkyline(buildings)

    buildings = [
        [1, 2, 1],
        [1, 2, 2],
        [1, 2, 3]
    ]
    s = Solution()
    # [[1,3],[2,0]]
    print s.getSkyline(buildings)

    buildings = [
        [2, 9, 10],
        [3, 7, 15],
        [5, 12, 12],
        [15, 20, 10],
        [19, 24, 8]]

    s = Solution()
    # [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    print s.getSkyline(buildings)

    buildings = [
        [0, 2, 3],
        [2, 5, 3]
    ]
    s = Solution()
    # [[0,3],[5,0]]
    print s.getSkyline(buildings)