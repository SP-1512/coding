class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        count = {}
        paragraph = paragraph.replace("."," ")
        paragraph = paragraph.replace(","," ")
        paragraph = paragraph.replace("!"," ")
        paragraph = paragraph.replace("?"," ")
        paragraph = paragraph.replace("'"," ")
        paragraph = paragraph.replace("/"," ")
        paragraph = paragraph.replace(";"," ")
        paragraph = list(paragraph.split( ))
        for i in paragraph:
            lower = i.lower()
            if lower in banned:
                continue
            elif lower.isalpha():
                count[lower] = count.get(lower, 0) + 1
        
        count = sorted(count.items(),key = lambda x:x[1],reverse = True)

        return str(count[0][0])