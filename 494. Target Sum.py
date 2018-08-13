class Solution(object):
    def findTargetSumWays(self, nums, S):
        if not nums:
            return 0
        pre_dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            new_dic = {}
            for pre in pre_dic:
                new_dic[pre + nums[i]] = new_dic.get(pre + nums[i], 0) + pre_dic.get(pre, 0)
                new_dic[pre - nums[i]] = new_dic.get(pre - nums[i], 0) + pre_dic.get(pre, 0)
            pre_dic = new_dic
        return new_dic.get(S, 0)

sol = Solution()
nums = [1, 1, 1, 1, 1]
# nums = [0, 1, 2, 3, 4]
S = 3
print(sol.findTargetSumWays(nums, S))

# if not nums:
#     return 0
# dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
# for i in range(1, len(nums)):
#     tdic = {}
#     for d in dic:
#         tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic.get(d,
#                                                                0)  # (exist sum count) + (existing sum count in previous level)
#         tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic.get(d, 0)
#     dic = tdic
# return dic.get(S, 0)
# if not nums:
#     return 0
# n = len(nums)
# res = 0
# dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
# for i in range(1, n+1):
#     dp[i][0] = dp[i-1][0] - nums[i-1]
#     res += 1 if dp[i][0] == S else 0
#     dp[0][i] = dp[0][i-1] + nums[i-1]
#     res += 1 if dp[0][i] == S else 0
#     for j in range(1, n):
#         dp[j][n-j] = dp[j-1][n-j] - nums[j-1] + dp[j][n-j-1] + nums[n-j-1]
#         res += 1 if dp[j][n-i] == S else 0
# print(dp)
# return res