class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_numbers = 0
        for i in range(0, len(nums)):
            if (len(str(nums[i])) % 2) == 0:
                even_numbers += 1
        return even_numbers
                
        
