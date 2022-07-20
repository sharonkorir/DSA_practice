class Solution(object):
    def merge(self, nums1, m, nums2, n):
        total_len = m + n
        for i in range(0, n):
            nums1.insert(i, nums2[i])
            nums1.pop()
        nums1.sort()
    
