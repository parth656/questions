import math
class Solution:
    def sortColors(self, nums: List[int]) -> None:
       
        n=len(nums)
        c=0
        d=0
        e=0
        for i in range(n):
            if nums[i]==0:
                c+=1
            elif nums[i]==1:
                d+=1
            else:
                e+=1
        i=0
        while(c>0):
            nums[i]=0
            i+=1
            c-=1
        
        while(d>0):
            nums[i]=1
            i+=1
            d-=1
        while (e>0):
            nums[i]=2
            i+=1
            e-=1