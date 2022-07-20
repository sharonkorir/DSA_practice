class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squared_arr = []
        for i in range(0,len(nums)):
            squared_arr.append((nums[i]*nums[i]))
        squared_arr.sort()
        return squared_arr
            
