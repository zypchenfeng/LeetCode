def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    S = S.replace("-", "").upper()[::-1]
    return '-'.join([S[i:i + K] for i in range(0, len(S), K)])[::-1]

S = "2-5g-3-J"
K = 2

# S = "5F3Z-2e-9-w"
# K = 4
print(licenseKeyFormatting(S, K))
