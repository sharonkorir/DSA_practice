class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        total_len = len(nums1)
        nums1[m:total_len] = nums2
        nums1.sort()
