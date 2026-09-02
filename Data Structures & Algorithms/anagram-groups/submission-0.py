class Solution:
    def groupAnagrams(self, strs):
        di = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in di:
                di[key] = []
            di[key].append(s)
        return list(di.values())