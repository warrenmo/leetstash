import itertools


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in itertools.zip_longest(
            map(int, version1.split('.')),
            map(int, version2.split('.')),
            fillvalue=0,
        ):
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0
