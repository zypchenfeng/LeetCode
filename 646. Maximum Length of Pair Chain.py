class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # # solution 1
        # pairs = sorted(pairs, key=lambda x: x[1])
        # cur = float('-inf')
        # res = 0
        # for pair in pairs:
        #     if cur < pair[0]:
        #         res += 1
        #         cur = pair[1]
        # return res

        # solution 2
        pairs = sorted(pairs)
        dp = [0]*len(pairs)
        res = 0
        for i in range(1, len(pairs)):
            dp[i] = max(0, pair[i+1][0] - pair[i][1]) + dp[i-1]
            res = max(res, dp[i])
        return res