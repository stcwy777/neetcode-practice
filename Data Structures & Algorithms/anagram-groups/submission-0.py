from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        rslt = defaultdict(list)
        for s in strs:
            k = [0] * 26
            for c in s:
                k[ord(c) - ord('a')] += 1
            rslt[tuple(k)].append(s)
        print(rslt.values())
        return list(rslt.values())