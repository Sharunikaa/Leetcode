class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        f=[0]*26
        for i in s:
            f[ord(i)-ord('a')]+=1
        for i in t:
            f[ord(i)-ord('a')]-=1
        for i in f:
            if i!=0:
                return False
        return True

        