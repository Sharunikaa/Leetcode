class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r=""
        s=sorted(strs)
        a=min(strs,key=len)
        b=min(a)
        first, last = s[0], s[-1]
        for j in range(b):
            if first[j] == last[j]:
                r += first[j]
            else:
                break
        return r
                
            