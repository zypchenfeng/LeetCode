class Solution(object):
    def waysToPaint(self, n, k):
        '''
        :param n: non-negative, number of posts to be painted
        :param k: non-negative, number of colors to choose from
        :return: total number of ways to paint when no more than 2 nearby posts with the same color
        '''
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

sol = Solution()
n = 2
k = 2
print(sol.waysToPaint(n, k))

n = 0
k = 0
print(sol.waysToPaint(n, k))

n = 1
k = 1
print(sol.waysToPaint(n, k))

n = 3
k = 4
print(sol.waysToPaint(n, k))