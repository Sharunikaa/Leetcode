class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if i!=j and j!=k and i!=k and nums[i]+nums[j]+nums[k]==0:
                        tmp=[nums[i],nums[j],nums[k]]
                        tmp.sort()
                        if tmp not in r:
                            r.append(tmp)
        return r
        