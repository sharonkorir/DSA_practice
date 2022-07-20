class Solution(object):
    def duplicateZeros(self, arr) :
        """
        Do not return anything, modify arr in-place instead.
        """
       
        l=len(arr)
        i=0
        while i<l:
            if arr[i]==0:
                arr.insert(i+1,0)
                arr.pop()
                i+=2
            else:
                i+=1
                
                    
            
        
