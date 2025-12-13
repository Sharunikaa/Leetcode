class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = min(strs, key=len)
        while prefix:
            if all(s.startswith(prefix) for s in strs):
                return prefix
            prefix = prefix[:-1]

        return ""
