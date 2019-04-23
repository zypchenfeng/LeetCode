class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = {r: i for i, r in enumerate(list1)}
        d2 = {r: i for i, r in enumerate(list2)}
        d3 = {r: d1[r] + d2[r] for r in d1 if r in d2}
        min_sum = min(d3.values())
        return [key for key in d3 if d3[key] == min_sum]

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
sol = Solution()
print(sol.findRestaurant(list1, list2))
