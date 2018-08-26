class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        Store the maximum score player1 can get for any sub array [i, j]

        Given an array A[i, j], player 1 can either take the first number A[i] or A[j],
        after that, it forms a new array A[i+1, j] or A[i, j-1] accordingly and it is player2's
        turn to pick up. The maximum score that player1 can get from the the sub arrays will be
        the larger one left by player2. So,

        DP formula:
        dp(i, j) = max(sum(i, j-1) - dp(i, j-1) + nums[j], sum(i+1, j) - dp(i+1, j) + nums[i])

        Because sum(i, j-1) + nums[j] = sum(i, j) = nums[i] + sum(i+1, j), the formula can be simplified to
        dp(i, j) = max(sum(i, j) - dp(i, j-1), sum(i, j) - dp(i+1, j))

        Thanks to @coder2 point out that the mistake of the dp formula deduction.
        If we do more deduction, we can eliminate the sum(i, j) from the formula:
        Instead of storing the maximum score that player 1 can get in each sub array, we can store the diff
        between player1 and player 2. For example: if player 1 get A, player 2 get B, we can use dp' to store A-B.

        if A = dp(i, j), then B = sum(i, j) - dp(i, j)

        So dp'(i, j) = dp(i, j) - ( sum(i, j) - dp(i, j) ) = 2*dp(i, j) - sum(i, j), so
        2*dp(i, j) = dp'(i, j) + sum(i, j) (this will be used below)

        dp'(i, j) = dp(i, j) - ( sum(i, j) - dp(i, j) ) = 2dp(i, j) - sum(i, j)
        = 2 * max( sum(i, j) - dp(i, j-1), sum(i, j) - dp(i+1, j) ) - sum(i, j)
        = max(sum(i, j) - 2*dp(i, j-1), sum(i, j) - 2*dp(i+1, j) )
        = max(sum(i, j) - ( dp'(i, j-1) + sum(i, j-1) ), sum(i, j) - ( dp'(i+1, j) + sum(i+1, j)))
        = max(sum(i, j) - sum(i, j-1) - dp'(i, j-1), sum(i, j) - sum(i+1, j) - dp'(i+1, j))
        = max(nums[j] - dp'(i, j-1), nums[i] - dp'(i+1, j))

        Final formula: dp(i, j) = max(nums[j] - dp(i, j-1), nums[i] - dp(i+1, j))
        """
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for l in range(1, n):
            for i in range(0, n - l):
                j = i + l
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][n - 1] >= 0