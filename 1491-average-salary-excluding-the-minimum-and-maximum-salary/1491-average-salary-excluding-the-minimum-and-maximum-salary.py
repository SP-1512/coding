class Solution:
    def average(self, salary: list[int]) -> float:
        ma = max(salary)
        mi = min(salary)
        n = len(salary)
        ave = 0
        c = 0
        for i in (salary):
            if i!= mi and i!= ma:
                ave += i
                c += 1
        return ave/c