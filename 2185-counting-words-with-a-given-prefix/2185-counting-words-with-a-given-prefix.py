class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        c = 0
        pl = len(pref)
        for i in words:
            if i.startswith(pref):
                c += 1
        return c