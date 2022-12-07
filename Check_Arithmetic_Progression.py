
class Solution:
    
    def checkIsAP(self, arr, n):
        arr=sorted(arr)
        m=arr[1]-arr[0]
        for i in range(1,n):
            if(arr[i]-arr[i-1]!=m):
                return 0
        return 1