#!/usr/bin/python

#returns index of z in arr if present - else it's -1
def binarySearch(arr, x, y, z):
    #check basecase
    if y >= x:
        mid = x + (y-1)/2
        # element is at the middle
        if arr[mid] == z:
            return mid
        # if element is smaller than middle  - it's in left part array
        elif arr[mid] > z:
            return binarySearch(arr, x, mid- 1, z)
        #else element is only present in right part  array
        else:
            return binarySearch(arr, mid + 1, y, z)
    else:
        return -1

#test array
arr = [2, 3, 4, 10, 40]
z = 10

result = binarySearch(arr, 0, len(arr)-1, z)

if result != -1:
    print "element is present at index %d" % result
else:
    print "element is not present in array"
