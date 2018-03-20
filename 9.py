class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return int(-self.isPalindrome(str(-x)))==x
        return int(str(x)[::-1])==x
        
