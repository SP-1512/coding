class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ll = []
        for i in range(0,len(words)):
            if x in words[i]:
                ll.append(i)
        return ll