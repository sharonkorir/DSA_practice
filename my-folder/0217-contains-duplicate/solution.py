class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_nums = set(nums)
        if len(my_nums) == len(nums):
            return False
        else:
            return True
        
