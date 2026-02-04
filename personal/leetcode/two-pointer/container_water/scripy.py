class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        m=0
        while l <r:
            width=r-l
            cont_h=min(h[l],h[r])
            curr_area=width*cont_h
            m=max(curr_area,m)
            if h[l]<h[r]:
                l+=1
            else:
                r-=1
        return m
        