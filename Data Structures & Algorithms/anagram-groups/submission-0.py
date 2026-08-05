class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = {}
        for i, val in enumerate(strs):
            key = "".join(sorted(val))
            A.setdefault(key, []).append(val)
    
        return list(A.values())