class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            k = "".join(sorted(i))
            ans[k].append(i)
        return list(ans.values())