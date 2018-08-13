class Solution(object):
    def PalSubstrings(self, s):
        '''
        Given a string, your task is to count how many palindromic substrings in this string.
        The substrings with different start indexes or end indexes are counted as different
        substrings even they consist of same characters.
        :param S: a string with length less than 1000
        :return: int, count of palindromic strings
        '''
        ans = 0
        left, right = 0, 0
        while left < len(s):
            # expand max right with same char as left
            while right < len(s) and s[right] == s[left]:
                right += 1
            same_len = right - left
            # add possible palindrom: 1 + 2 + ... + same_len
            ans += (same_len * (same_len + 1)) // 2

            # expand palindrom based on the consecutive chars
            l, r = left - 1, right
            while l >= 0 and r < len(s) and s[r] == s[l]:
                ans += 1
                l -= 1
                r += 1

            # slide to next index after consecutive chars
            left = right
        return ans




sol = Solution()
s1 = 'abc'
s2 = 'aaa'
s3 = 'abcabc'
print(sol.PalSubstrings(s1))
print(sol.PalSubstrings(s2))
print(sol.PalSubstrings(s3))