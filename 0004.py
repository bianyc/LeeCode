# -*- coding: utf-8 -*-
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :return: float
        """
        if not nums1 and not nums2:
            return

        nums = nums1 + nums2
        nums.sort()

        if len(nums) % 2 == 0:
            n = int(len(nums) / 2)
            media = float((nums[n] + nums[n - 1]) / 2)
        else:
            media = float(nums[int(len(nums) / 2)])

        return media

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1], []))
