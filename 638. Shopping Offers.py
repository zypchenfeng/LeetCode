class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        if not price or not needs or len(price) != len(needs):
            return 0
        if not special:
            res = 0
            for i in range(len(price)):
                res += price[i]*needs[i]
            return res

        d = {}
        res = dfs(needs)
        def dfs(cur):
            val = sum(cur[i] * price[i] for i in range(len(needs)))  # cost without special
            for spec in special:
                tmp = [cur[j] - spec[j] for j in range(len(needs))]
                if min(tmp) >= 0:  # skip deals that exceed needs
                    val = min(val, d.get(tuple(tmp), dfs(tmp)) + spec[
                        -1])  # .get check the dictionary first for result, otherwise perform dfs.
            d[tuple(cur)] = val
            return val

        return res


sol = Solution()
price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print('Right answer should be 14  ', sol.shoppingOffers(price, special, needs))


price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]
print('Right answer should be 11  ',sol.shoppingOffers(price, special, needs))

price = [2,3,4]
special = []
needs = [1,2,1]
print('Right answer should be 12  ',sol.shoppingOffers(price, special, needs))