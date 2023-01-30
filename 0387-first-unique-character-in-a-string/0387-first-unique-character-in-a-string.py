from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        counter = Counter(s)
        i = 0
        for c in s:
            if counter[c] == 1:
                return i
            i += 1
        return -1
        