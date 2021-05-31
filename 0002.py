# -*- coding: utf-8 -*-

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        num1 = self.get_int(l1)
        num2 = self.get_int(l2)

        num = num1 + num2

        res = []
        for s in str(num):
            res.append(int(s))
        return res[::-1]

    def get_int(self, nums):
        nums_ = []
        for i in nums:
            nums_.append(str(i))
        num = int("".join(nums_))
        return num

if __name__ == '__main__':
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    s = Solution()
    print(s.addTwoNumbers(l1, l2))

