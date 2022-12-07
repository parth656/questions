class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        for i in range(len(nums)):
           x^=nums[i]
        temp=1
        while(temp&x==0):
            temp=temp<<1
        a=0
        b=0
        for i in range(len(nums)):
            if(temp&nums[i]==0):
                a^=nums[i]
            else:
                b^=nums[i]
        return a,b