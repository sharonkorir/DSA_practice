class Solution(object):
    def maxSubArray(self, nums):
        answer = nums[0]
        sub_arr = nums[0]

        for i in range(1, len(nums)):
            sub_arr = max(nums[i], nums[i] + sub_arr)
            answer = max(answer, sub_arr)
    
        return answer
        
