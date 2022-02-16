'''
1. Traverse the array once and keep updating the frequency of array 
elements in the Map.

2. Check if the size of the map is equal to the total number of 
distinct elements present in the original array or not. If found 
to be true, update the maximum sum.

3. While traversing the original array, if the ith traversal crosses 
K elements in the array, update the Map by deleting an occurrence of 
(i – K)th element.

4. After completing the above steps, print the maximum sum obtained.
'''

# Python 3 program for the above approach
 
# Function to count the number of
# distinct elements present in the array
def distinct(arr, N):
    st = set()
     
    # Insert array elements into set
    for i in range(N):
        st.add(arr[i])
 
    # Return the st size
    return len(st)

# Function to calculate maximum
# sum of K-length subarray having
# same unique elements as arr[]
def maxSubarraySumUtil(arr, N, K, totalDistinct):
    # Not possible to find an
    # subarray of length K from
    # an N-sized array, if K > N
    if (K > N):
        return 0
 
    mx = 0
    sum = 0
 
    mp = {}
 
    # Traverse the array
    for i in range(N):
        # Update the mp
        if(arr[i] in mp):
            mp[arr[i]] += 1
        else:
            mp[arr[i]] = 1
        sum += arr[i]
 
        # If i >= K, then decrement
        # arr[i-K] element's one
         # occurence
        if (i >= K):
            if(arr[i-K] in mp):
                mp[arr[i - K]] -= 1
                sum -= arr[i - K]
 
            # If frequency of any
            # element is 0 then
            # remove the element
            if (arr[i-K] in mp and mp[arr[i - K]] == 0):
                mp.remove(arr[i - K])
 
        # If mp size is same as the
        # count of distinct elements
        # of array arr[] then update
        # maximum sum
        if (len(mp) == totalDistinct):
            mx = max(mx, sum)
    return mx
 
# Function that finds the maximum
# sum of K-length subarray having
# same number of distinct elements
# as the original array
def maxSubarraySum(arr, K):
   
    # Size of array
    N = len(arr)
    # Stores count of distinct elements
    totalDistinct = distinct(arr, N)
 
    # Print maximum subarray sum
    print(maxSubarraySumUtil(arr, N, K, totalDistinct))
 
# Driver Code
if __name__ == '__main__':
    arr  =  [7, 7, 2, 4, 2,7, 4, 6, 6, 6]
    K = 6
 
    # Function Call
    maxSubarraySum(arr, K)