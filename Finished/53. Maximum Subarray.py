class Solution(object):
    def maxSubarray(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return nums
        dp = [0]*n
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], 0) + nums[i]
            res = max(res, dp[i])
        return max(dp[:])

sol = Solution()
nums = [1, -3, 2, 1, 5, -6]
print(sol.maxSubarray(nums))