class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1
        output = ""
        count = sorted(count.items(),key=lambda x:x[1],reverse=True)

        for i,j in count:
            output = output + str(i)*int(j)

        return output