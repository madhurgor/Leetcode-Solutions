class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return -self.reverse(-x)
        else:
            t = int(str(x%2**31)[::-1])
            if t > 2**31-1 or t < -(2**31):
                return 0
            else:
                return t
