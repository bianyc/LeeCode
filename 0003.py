# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 1
        son_str = ""

        for x in s:
            if x not in son_str:
                son_str += x
                if len(son_str) > max_len:
                    max_len = len(son_str)
            else:
                if len(son_str) > max_len:
                    max_len = len(son_str)
                son_str += x
                index = son_str.index(x) + 1
                son_str = son_str[index:]
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("aucauv"))
