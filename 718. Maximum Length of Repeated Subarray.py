class Solution(object):
    def findLength(self, A, B):
        '''
        Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays
        Input:
        A: [1,2,3,2,1]
        B: [3,2,1,4,7]
        Output: 3
        Explanation:
        The repeated subarray with maximum length is [3, 2, 1].
        :param A:
        :param B:
        :return:
        '''
        # solution 1
        if not A or not B:
            return 0
        A,res,sub = '#' + '#'.join(map(str,A)) + '#', 0, '#'
        #print (A)
        for ch in B:
            sub += str(ch) + '#'
            if sub in A:
                res += 1
            else:
                sub = sub[sub[1:].index('#') + 1:]
        return res
        # solution2
        # if not A or not B:
        #     return 0
        # dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
        # res = 0
        # for i in range(1, len(A)+1):
        #     for j in range(1, len(B)+1):
        #         if A[i-1] == B[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #             res = max(res, dp[i][j])
        # return res

A = [1,2,3,2,1]
B = [3,2,1,4,7]
sol = Solution()
print(sol.findLength(A, B))