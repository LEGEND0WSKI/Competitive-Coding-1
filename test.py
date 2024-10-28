arr = [1,2,3,5,6,7,8]
# [11,12,13,15,16,17,18]
# [0, 1, 2, 3, 4, 5, 6]
#  Output = 4
h = len(arr)-1
l = 0

while h-l>1:
    mid = l +(h-l)//2	 #3 index,
    if arr[mid] - arr[l] != mid - l: #left missing
        h = mid 
    else:
        l = mid 
    
print(arr[l]+1)
