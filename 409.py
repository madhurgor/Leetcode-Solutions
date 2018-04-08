class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        oddFlag=False
        c=0
        for i in d:
            if d[i]%2==0:
                c+=d[i]
            else:
                c+=d[i]-1
                oddFlag=True
        if oddFlag:
            return c+1
        return c
