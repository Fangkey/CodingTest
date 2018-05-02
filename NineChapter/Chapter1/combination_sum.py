class Solution(object):
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


if __name__ == "__main__":
    s = Solution()
    print s.combinationSum([2, 3, 7], 7)