class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # solution 1
        pairs = sorted(pairs, key=lambda x: x[1])
        cur = float('-inf')
        res = 0
        for pair in pairs:   #use greedy algorithm
            if cur < pair[0]:
                res += 1
                cur = pair[1]
        return res