class Solution:
    def sep(self, i, ll):
        i = str(i)
        for digit in str(i):
            ll.append(int(digit))

    def separateDigits(self, nums: list[int]) -> list[int]:
        ll = []
        for i in nums:
            if i <= 9:
                ll.append(i)
            else:
                self.sep(i, ll)
        return ll