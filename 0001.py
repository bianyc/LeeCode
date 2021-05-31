# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, num in enumerate(nums):
            for i in range(index + 1, len(nums)):
                if num + nums[i] == target:
                    return [index, i]



if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))
