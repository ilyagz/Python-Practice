/*
9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

*/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        flag = 0
        for i in range(0, len(y)//2):
            if (y[i] != y[len(y)-i-1]):
                return False
        return True
                