class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_nums = 0
        ans = []
        for i in range(len(nums)):
            sum_nums += nums[i]
            ans.append(sum_nums)
        return ans
            
