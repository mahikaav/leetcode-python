class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mind = m - 1
        nind = n - 1
        right = m + n -1

        while nind >=0:
            if mind >= 0 and nums1[mind] > nums2[nind]:
                nums1[right] = nums1[mind]
                mind -= 1
            else:
                nums1[right] = nums2[nind]
                nind -= 1
            
            right -= 1

        