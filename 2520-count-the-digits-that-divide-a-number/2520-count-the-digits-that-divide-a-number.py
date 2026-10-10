class Solution:
    def countDigits(self, num: int) -> int:
        output = "".join(sorted(str(num)))
        for i in str(num):
            if i not in output:
                output += str(i)
        count = 0
        for i in output:
            num1 = int(i)
            if num%num1 == 0:
                    count = count + 1
        return count