# works on the principal of repeated multiplication to find if the number is a multiple or not 
# Can be done using repeated division also or using log
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        counter = 1
        while counter < n:
            counter *=4
        return counter == n
