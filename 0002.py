# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 直接将对应链表元素进行相加，就正好相当于从个位数开始往上面加
        node = ListNode(0)
        pointer = node
        carry = 0
        while l1 != None or l2 != None:
            # 那么向后移动到None了后，l2将不会具有val值，这该如何处理？
            if l1 != None and l2 != None:
                if (l1.val + l2.val + carry) >= 10:
                    node.next = ListNode(l1.val + l2.val + carry - 10)
                    node = node.next
                    carry = 1
                if (l1.val + l2.val + carry) < 10:
                    node.next = ListNode(l1.val + l2.val + carry)
                    node = node.next
                    carry = 0
            if l1 == None:
                if (l2.val + carry) >= 10:
                    node.next = ListNode(l2.val + carry - 10)
                    node = node.next
                    carry = 1
                if (l2.val + carry) < 10:
                    node.next = ListNode(l2.val + carry)
                    node = node.next
                    carry = 0
            if l2 == None:
                if (l1.val + carry) >= 10:
                    node.next = ListNode(l1.val + carry - 10)
                    node = node.next
                    carry = 1
                if (l1.val + carry) < 10:
                    node.next = ListNode(l1.val + carry)
                    node = node.next
                    carry = 0
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        if carry == 1:
            node.next = ListNode(1)
            node = node.next

        return pointer.next

# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: List
#         :type l2: List
#         :return: List
#         """
#
#         num1 = self.get_int(l1)
#         num2 = self.get_int(l2)
#
#         num = num1 + num2
#
#         res = []
#         for s in str(num):
#             res.append(int(s))
#         return res[::-1]
#
#     def get_int(self, nums):
#         nums_ = []
#         for i in nums:
#             nums_.append(str(i))
#         num = int("".join(nums_))
#         return num
#
# if __name__ == '__main__':
#     l1 = [9,9,9,9,9,9,9]
#     l2 = [9,9,9,9]
#     s = Solution()
#     print(s.addTwoNumbers(l1, l2))
