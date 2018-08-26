class Solution:
    def largestDivisibleSubset(self, nums):
        # solution 2
        # dp =[[]]
        # for num in sorted(nums):
        #     dp
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))

nums = [1, 2, 3, 4, 6, 9, 16, 8]
sol = Solution()
print(sol.largestDivisibleSubset(nums))