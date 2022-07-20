class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        answer = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                count = 0
            else:
                count +=1
                print(count)
                answer = max(answer, count)
        return answer
        
