class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        output = ""
        out = ""
        
        for j in sorted(freq.values()):
            if str(j) not in output:
                output = output + str(j) + ","
                out = out + str(j) + ","
            else:
                out = out + str(j) + ","
        
        if output == out:
            return True
        else:
            return False