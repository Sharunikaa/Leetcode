class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i,j in enumerate(numbers):
            x=target-j
            if x in d:
                return[d[x]+1,i+1]
            d[j]=i