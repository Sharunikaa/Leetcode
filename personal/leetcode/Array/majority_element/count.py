class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        m=0
        for i in set(nums):
            c=nums.count(i)
            d[i]=c
            m=max(m,c)
        for k,val in d.items():
            if val==m:
                return k
        

            