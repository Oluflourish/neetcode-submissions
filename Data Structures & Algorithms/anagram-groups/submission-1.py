class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1

            res[tuple(count)].append(s)
        
        return list(res.values())
        


    
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        A = {}
        for i, val in enumerate(strs):
            key = "".join(sorted(val))
            A.setdefault(key, []).append(val)
    
        return list(A.values())