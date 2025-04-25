class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_list = []
        k = 0 
        for i in range(len(nums)):
            if nums[i] not in set_list:
                set_list.append(nums[i])
                nums[k] = nums[i]
                k += 1
        return k
               


