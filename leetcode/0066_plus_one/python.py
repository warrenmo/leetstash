class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = list(digits)

        for i in reversed(range(len(res))):
            if res[i] != 9:
                res[i] += 1
                return res

            res[i] = 0

        res[0] = 1
        res.append(0)

        return res
