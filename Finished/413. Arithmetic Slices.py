class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        curr, sum = 0, 0
        for i in range(2,len(A)):
            if A[i]-A[i-1] == A[i-1]-A[i-2]:
                curr += 1
                sum += curr
            else:
                curr = 0
        return sum
        # if len(A) < 2:
        #     return 0
        # if len(A) == 2:
        #     return 1
        # else:
        #     dp = [0]*len(A)
        #     dp[1] = 1
        #     dp[2] = 1
        #     delta = 0
        #     pre_delta = A[1]-A[0]
        #     res = 0
        #     for i in range(3, len(A)):
        #         delta = A[i]- A[i-1]
        #         if delta == pre_delta:
        #             print(dp)
        #             dp[i] = sum(dp[:i-1])+1
        #             if dp[i] > res:
        #                 res = dp[i]
        #         else:
        #             pre_delta = delta
        #             dp[i] = 1
        #             dp[i-1] = 0
        #     return max(dp)

sol = Solution()
print(sol.numberOfArithmeticSlices([-10, -1]))
print(sol.numberOfArithmeticSlices([1,2,3]))
print(sol.numberOfArithmeticSlices([1,2,3,4]))