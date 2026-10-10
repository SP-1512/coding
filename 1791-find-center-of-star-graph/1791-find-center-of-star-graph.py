class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        ll = []
        for i in range(0,len(edges)):
            for j in range(0, 2):
                ll.append(edges[i][j])
        
        freq = {}
        for i in ll:
            freq[i] = freq.get(i, 0) + 1
        
        max_key = max(freq, key=freq.get)
        return(max_key) 