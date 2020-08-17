from itertools import combinations
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        comb = combinations(nums, 3)
        min_diff = ""
        res = 0
        for e in comb:
            soma = e[0] + e[1] + e[2]
            if soma == target:
                return soma
            elif min_diff != "" and abs(target-soma) < min_diff:
                res = soma
                min_diff = abs(target-soma)
            elif min_diff == "":
                res = soma
                min_diff = abs(target-soma)
        return res