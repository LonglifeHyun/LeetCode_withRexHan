# 557. Reverse Words in a String III

class Solution(object):
    def reverseWords(self, s):
        rlst_str = ""
        for word in s.split():
            rlst_str += word[::-1] + " "
        return rlst_str.strip()
