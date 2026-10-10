class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        ans = 0
        for i in range(0,len(endTime)):
            if endTime[i] >= queryTime and startTime[i] <= queryTime:
                ans += 1
        return ans