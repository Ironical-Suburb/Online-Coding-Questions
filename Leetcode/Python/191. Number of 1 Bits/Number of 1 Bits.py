class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        target = 1
        for i in range(32):
            if n & target != 0:
                counter += 1
            target <<= 1
        return counter
