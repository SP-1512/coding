class Solution:
    def calPoints(self, operations: list[str]) -> int:
        ans = []
        for i in operations:
            if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
                ans.append(int(i))
            elif i == "C":
                ans.pop()
            elif i == "D":
                l = ans[-1]
                ans.append(int(l*2))
            elif i == "+":
                x = ans[-1] + ans[-2]
                ans.append(int(x))
        return sum(ans)