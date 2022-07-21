class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        arr = []
        if x >= 0:
            for i in str(x):
                    arr.append(int(i))
            reversed_arr = arr[::-1]
            if (arr == reversed_arr):
                return True
            else:
                return False
