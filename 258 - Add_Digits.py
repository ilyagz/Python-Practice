# 258. Add Digits

# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0: return 0
        else:
            return int(num - 9 * math.floor ((num-1)/9)) 
            