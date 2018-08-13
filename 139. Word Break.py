class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for word in wordDict:
                if dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
        return dp[-1]

        # if s in wordDict:
        #     return True
        # else:
        #     i = 0
        #     while i < len(s):
        #         print(s[:i])
        #         if str(s[:i]) in wordDict and self.wordBreak(str(s[i:]), wordDict):
        #             return True
        #         i += 1
        #     return False
        

sol = Solution()
s = 'leetcode'
wordDict = ["leet", "code"]
print(sol.wordBreak(s, wordDict))
s = 'applepenapple'
wordDict = ["apple", "pen"]
print(sol.wordBreak(s, wordDict))
s = 'catsandog'
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(sol.wordBreak(s, wordDict))