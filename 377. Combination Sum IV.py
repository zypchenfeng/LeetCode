class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        calculated = {}
        for num in nums:
            calculated[str(num)] = 1
        cumu = 0
        if calculated.get(target, 0) == 0:
            for num in nums:
                cumu += self.combinationSum4(nums, target - num)
            calculated[str(target)] = cumu
        return calculated.get(target)

sol =Solution()
nums = [1, 2, 3]
target = 4
print(sol.combinationSum4(nums, target))