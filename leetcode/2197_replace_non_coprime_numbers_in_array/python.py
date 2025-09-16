import math
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            while True:
                g = math.gcd(num, res[-1] if res else 1)
                if g == 1:
                    break
                num *= res.pop() // g
            res.append(num)
        return res

