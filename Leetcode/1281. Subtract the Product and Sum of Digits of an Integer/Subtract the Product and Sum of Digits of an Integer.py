class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return prod(list(map(int, str(n))))-sum(list(map(int, str(n))))
        
