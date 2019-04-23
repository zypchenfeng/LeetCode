        if not costs or len(costs) == 0:
            return 0
        n = len(costs)
        dp = [[0]*3]*n
        dp[0] = costs[0]
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
			
	        return min(dp[n-1])
			
			
        if not n or not k:
            return 0
        diff = k           # if only one post, then no way to pain it the same
        same = 0
        res = same + diff
        for i in range(2, n+1):  # from 2nd post
           same = diff           # if the ith post need to be the same as previous color, then choices also the same as previous
           diff = res*(k-1)      # since it needs to be different, so only has k-1 choices
           res = same + diff     # the result will be merge of paint the same and different
        return res