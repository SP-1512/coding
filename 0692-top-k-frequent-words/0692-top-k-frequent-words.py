class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        ll = []

        count = {}
        words = sorted(words)
        for i in words:
            count[i] = count.get(i, 0) + 1

        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        if len(words) == k:
            return words
        
        for i in range(0,k):
            ll.append(str(count[i][0]))

        return ll     