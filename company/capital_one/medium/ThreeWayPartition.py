'''
Given an array and a range [lowVal, highVal], partition the array around the 
range such that array is divided in three parts. 
1) All elements smaller than lowVal come first. 
2) All elements in range lowVal to highVVal come next. 
3) All elements greater than highVVal appear in the end. 
The individual elements of three sets can appear in any order.
'''
def threeWayPartitiion(arr, lowVal, highVal):
    l, r = 0, len(arr) - 1
    i = 0
    while i <= r:

        # If the current position is smaller than range, put it or 
        # next available smaller position
        if arr[i] < lowVal:
            temp = arr[i]
            arr[i] = arr[l]
            arr[l] = arr[i]
            i += 1
            l += 1
        
        # If current element is greater than
        # range, put it on next available greater
        # position.
        elif arr[i] > highVal:
            temp = arr[i]
            arr[i] = arr[l]
            arr[l] = arr[i]
            r -= 1
            
        else:
            i += 1