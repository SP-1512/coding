class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = {}
        out = ""
        for i in nums:
            if str(i) not in out:
                out = out + str(i)
                dic[i] = 1
            else:
                dic[i] = dic.get(i, 0) + 1
        flag = False
        for i in dic.values():
            if i >= 2:
                flag = True

        return flag
        