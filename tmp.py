from collection import Counter
from itertools import combinations

class Solution(object):
    def numIdenticalPairs(self, nums):
        num_cnter = Counter(nums)

        answer = 0
        for v in num_cnter.values():
            tmp_list = [_ for i in range(v)]
            com_rslt = list(combinations(tmp_list, 2))
            answer += len(com_rslt)

        return answer
