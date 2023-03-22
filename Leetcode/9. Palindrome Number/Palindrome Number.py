class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x[::1] == x[::-1]:
                return True
        else:   
            return False
