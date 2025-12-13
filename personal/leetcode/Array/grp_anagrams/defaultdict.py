class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            a=''.join(sorted(i))
            d[a].append(i)
            print(d)
        return list(d.values())

            
        