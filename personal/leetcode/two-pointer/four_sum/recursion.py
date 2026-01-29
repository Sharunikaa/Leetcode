class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad,res=[],[]
        def kSum(k,start,target):
            if k==2:
                l,r=start,len(nums)-1
                while l<r:
                    t=nums[l]+nums[r]
                    if t==target:
                        res.append(quad+[nums[l],nums[r]])
                        l+=1
                        r-=1

                        while l<r and nums[l]==nums[l-1]:
                            l+=1
                        while l<r and nums[r]==nums[r+1]:
                            r-=1
                    elif t<target:
                        l+=1
                    else:
                        r-=1
                return
            
            for i in range(start,len(nums)-k+1):
                if i>start and nums[i]==nums[i-1]:
                    continue
                quad.append(nums[i])
                kSum(k-1,i+1,target-nums[i])
                quad.pop()
            
        kSum(4,0,target)
        return res

