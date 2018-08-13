class Solution(object):
    def maxSubarray(self, nums):
        if len(nums) < 2:
            return nums
        res = nums[0]
        dp = [0]*len(nums)
        # dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i-1]) + nums[i]
            res = max(res, dp[i])
        return res
sol = Solution()
nums = [1, -3, 2, 1, 5, -6]
print(sol.maxSubarray(nums))