class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # solution 1
        res = []
        candidates.sort()
        def dfs(remain, path):
            if remain == 0:
                res.append(path)
                return

            for num in candidates:
                if remain < num:   # candidates are ordered, if remain smaller than num, not possible have solution
                    break
                if path and num < path[-1]:  # if smaller than last candidate, then no need to look at this number
                    continue
                else:
                    dfs(remain - num, path + [num])
            return
        dfs(target, [])
        return res


        # solution 2
    #     candidates.sort()
    #     res = []
    #     self.dfs(candidates, target, 0, [], res)
    #     return res
    #
    #
    # def dfs(self, candidates, target, index, path, res):
    #     if target < 0:
    #         return
    #     elif target == 0:
    #         res.append(path)
    #         return
    #     else:
    #         for i in range(index, len(candidates)):
    #             self.dfs(candidates, target - candidates[i], i, path+[candidates[i]], res)

sol = Solution()

candidates = [2,3,6,7]
target = 7

results = sol.combinationSum(candidates, target)
for res in results:
    print(res)