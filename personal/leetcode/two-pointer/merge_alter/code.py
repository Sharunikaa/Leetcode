class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        p,q=0,0
        while p<len(word1) and q<len(word2):
            res+=word1[p]
            res+=word2[q]
            p+=1
            q+=1
        if len(word1)>len(word2):
            res+=word1[p:]
        elif len(word2)>len(word1):
            res+=word2[q:]
        return res