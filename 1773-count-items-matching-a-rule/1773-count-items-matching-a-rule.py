class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        idx = 0
        if ruleKey=="type":
            idx=0
        elif ruleKey=="color":
            idx=1
        else:
            idx=2
        count = 0
        for i in range(0, len(items)):
            if items[i][idx] == ruleValue:
                count += 1
        
        return count

        