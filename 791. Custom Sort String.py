# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
#
# S was sorted in some custom order previously. We want to permute the characters of T so that
#
# they match the order that S was sorted. More specifically, if x occurs before y in S, then x
#
# should occur before y in the returned string.
#
# Return any permutation of T (as a string) that satisfies this property.

# Example :
# Input:
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.

# Note:
#
# S has length at most 26, and no character is repeated in S.
# T has length at most 200.
# S and T consist of lowercase letters only.

# Need to use heap sort
def customSortString(S, T):
    m = {k : idx for idx, k in enumerate(S)}
    q = []
    for t in T:
        if t not in m:
            q.append([26, t])
        else:
            q.append([m[t], t])
    q.sort(key=lambda x : x[0])
    res = ''
    for row in q:
        res += row[1]
    return res


S = "cba"
T = "abcd"
print(customSortString(S, T))
