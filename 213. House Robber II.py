class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #solution1
        if len(nums) == 1:
            return nums[0]
        rob = 0
        no_rob = 0
        for i in range(len(nums) - 1):
            next_rob = no_rob + nums[i]
            no_rob = max(no_rob, rob)
            rob = next_rob
        res = max(rob, no_rob)
        rob = 0
        no_rob = 0
        for i in range(1, len(nums)):
            next_rob = no_rob + nums[i]
            no_rob = max(no_rob, rob)
            rob = next_rob
        res = max(res, rob, no_rob)
        return res
        # solution 2
    #     if not nums:
    #         return 0
    #     return max(self.helper(nums[:-2]), self.helper(nums[1:]))
    #
    # def helper(self, nums):
    #     n = len(nums)
    #     if n == 0:
    #         return 0
    #     if n < 3:
    #         return max(nums)
    #     dp = [0]*n
    #     dp[0] = nums[0]
    #     dp[1] = max(nums[0], nums[1])
    #     for i in range(1, n):
    #         dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    #     return dp[-1]

