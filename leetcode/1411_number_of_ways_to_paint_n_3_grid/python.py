class Solution:
    def numOfWays(self, n: int) -> int:
        same = diff = 6
        MOD = int(1e9 + 7)

        for _ in range(n - 1):
            new_same = (3 * same + 2 * diff) % MOD
            new_diff = (2 * same + 2 * diff) % MOD
            same, diff = new_same, new_diff

        return (same + diff) % MOD
