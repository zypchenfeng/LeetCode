def checkPerfectNumber(num):
    """
    :type num: int
    :rtype: bool
    """
    if num <= 1:
        return False
    else:
        mid = 2
        sum = 1
        while mid**2 <= num:
            if num%mid == 0:
                sum += (mid + num/mid)
            mid += 1
    return sum == num

test = 6
print(checkPerfectNumber(test))