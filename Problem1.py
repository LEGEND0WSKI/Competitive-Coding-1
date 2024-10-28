# An array without duplicate elements. Find missing elemnt.
# Bruteforce is iterative search difference between index and element.
# We use Binary search to find index difference between low and highs with middle element.
# [1, 2, 3, 5, 6, 7, 8] OG array
# [0, 1, 2, 3, 4, 5, 6] index
#  Output = 4

class Solution:
    def missingItem(self, arr:list) -> int:
            
        high = len(arr)-1
        low = 0

        while high-low>1:
            mid = low +(high-low)//2	           
            if arr[mid] - arr[low] != mid - low:   # left of mid is missing 
                high = mid                                  
            else:                                  # right of mid is missing
                low = mid                          
            
        return arr[low]+1

arr = [1,2,3,5,6,7,8]
x = Solution().missingItem(arr)
print(x)