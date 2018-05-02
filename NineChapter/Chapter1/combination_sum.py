class Solution1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates = sorted(candidates)
        self.helper(candidates, [], 0, target, result)
        return result

    def helper(self, candidates, cur_set, cur_index, cur_target, result):
        for i in range(cur_index, len(candidates)):
            cur_cand = candidates[i]
            if cur_cand < cur_target:
                cur_set.append(cur_cand)
                self.helper(candidates, cur_set, i, cur_target - cur_cand, result)
            elif cur_cand > cur_target:
                return
            elif cur_cand == cur_target:
                solution = cur_set[:]
                solution.append(cur_cand)
                result.append(solution)
                return
            cur_set.pop()



# 2018-05-03 00:05
# 2018-05-03 00:15

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ret_list = []
        cur_set = []
        candidates = sorted(candidates)
        self.helper(candidates, 0, cur_set, target, ret_list)
        return ret_list

    def helper(self, candidates, cur_index, cur_set, target, ret_list):
        if target == 0:
            ret_list.append(cur_set[:])

        for i in range(cur_index, len(candidates)):
            c = candidates[i]
            if target >= c:
                cur_set.append(c)
                self.helper(candidates, i, cur_set, target - c, ret_list)
                cur_set.pop()



if __name__ == "__main__":
    s = Solution()
    # [[2, 2, 3], [7]]
    print s.combinationSum([2, 3, 7], 7)
    # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print s.combinationSum([2, 3, 5], 8)