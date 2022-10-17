class Solution(object):
    def runningSum(self, nums):
        sum_nums = 0
        ans = []
        for i in range(len(nums)):
            sum_nums += nums[i]
            ans.append(sum_nums)
        return ans

