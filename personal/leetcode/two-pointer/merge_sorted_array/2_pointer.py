class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l,r,n=m-1,n-1,len(nums1)-1
        while(r>=0):
            if l>=0 and nums1[l]>nums2[r]:
                nums1[n]=nums1[l]
                l-=1
            if r>=0 and nums2[r]>nums1[l]:
                nums1[n]=nums2[r]
                r-=1
            n-=1
         


        