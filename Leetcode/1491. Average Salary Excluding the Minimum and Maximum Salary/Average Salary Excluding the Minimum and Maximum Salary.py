class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        highest = salary[0]
        lowest = salary[0]
        total = 0
        for i in range(len(salary)):
            if highest < salary[i]:
                highest = salary[i]
            if lowest > salary[i]:
                lowest = salary[i]
        salary.pop(salary.index(highest))
        salary.pop(salary.index(lowest))
        sum_salary = sum(salary)
        average=sum_salary/len(salary)
        average = round(average,5)
        return average
