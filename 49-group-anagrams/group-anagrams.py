class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        countDict = defaultdict(list)
        for string in strs:
            countString = "".join(sorted(string))
            countDict[countString].append(string)
        return countDict.values()
        