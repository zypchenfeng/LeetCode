class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        counter = 0
        if len(A) != len(B):
            return False
        for i in range(len(A)):
            a = A[i]
            b = B[i]
            if a != b:
                if counter == 0:
                    t1 = a
                    t2 = b
                    counter += 1
                elif counter == 1 and t1 == b and t2 == a:
                    counter += 1
                else:
                    return False
        # if len(A) == 2:
        #     if counter == 2:
        #         return False
        #     if counter == 0:
        #         return True
        return counter==2 or counter == 0

sol = Solution()

A = "ab"
B = "ba"
print(sol.buddyStrings(A, B))

A = "ab"
B = "ab"
print(sol.buddyStrings(A, B))

A = "aa"
B = "aa"
print(sol.buddyStrings(A, B))

A = "aaaaaaabc"
B = "aaaaaaacb"
print(sol.buddyStrings(A, B))

A = ""
B = "aa"
print(sol.buddyStrings(A, B))