class Solution(object):
    def helper(self, candidates, cur_target, cur_index, cur_solution, result):
        if cur_target == 0:
            sorted_solution = cur_solution[:]
            sorted_solution = sorted(sorted_solution)
            if sorted_solution not in result:
                result.append(sorted_solution)
            return

        for i in range(cur_index, len(candidates)):
            cur_num = candidates[i]
            if cur_num <= cur_target:
                cur_solution.append(cur_num)
                if cur_solution == [1]:
                    pass
                self.helper(candidates, cur_target - cur_num, i + 1, cur_solution, result)
                cur_solution.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(candidates, target, 0, [], result)
        return result


if __name__ == "__main__":
    s = Solution()

    cand = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    # [
    #   [1, 7],
    #   [1, 2, 5],
    #   [2, 6],
    #   [1, 1, 6]
    # ]
    
    print s.combinationSum2(cand, target)

    cand = []
    target = 8
    print s.combinationSum2(cand, target)

    cand = [1]
    target = 8
    print s.combinationSum2(cand, target)


