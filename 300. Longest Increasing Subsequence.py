class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tails = [0] * (len(nums)+1)
        tails[0] = nums[0]
        res = 0
        for num in nums:
            if num < tails[0]:
                tails[0] = num
            elif num > tails[res]:
                tails[res+1] = num
                res += 1
            else:
                start = -1
                end = res
                while start < end-1:
                    m = (start+end)//2
                    if tails[m] >= num:
                        end = m
                    else:
                        start = m
                tails[start+1] = num
        return res+1

sol = Solution()
nums = [10,9,2,5,3,7,101,18, 1, 2]
print(sol.lengthOfLIS(nums))