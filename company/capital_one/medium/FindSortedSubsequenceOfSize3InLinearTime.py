'''
Given an array of n integers, find the 3 elements such that a[i] < a[j] < a[k] 
and i < j < k in 0(n) time. If there are multiple such triplets, then print 
any one of them.
'''


def findThreeNumbers(nums):
    # If number of elements < 3
    # then no triplets are possible
    if (len(nums) < 3):
        print("No such triplet found", end = '')
        return
    seq = 1   
    min_num = nums[0]
    # Least max number in best sequence
    # i.e. track arr[j] (e.g. in
    # array {1, 5, 3} our best sequence
    # would be {1, 3} with arr[j] = 3)
    max_seq = -float('inf')
    store_min = min_num  

    # Iterate
    for i in range(1, len(nums)):
        if nums[i] == min_num:
            continue
        elif nums[i] < min_num:
            min_num = nums[i]
            continue
        # This condition is only hit
        # when current sequence size is 2
        elif(nums[i] < max_seq):    
            # Update best sequence max numberto a smaller value (i.e. we've found a
            # smaller value for arr[j])
            max_seq = nums[i]   
            store_min = min_num                  

        # Increase best sequence length &
        # save next number in our triplet
        elif (nums[i] > max_seq):
            if seq == 1:
                store_min = min_num
            seq += 1
            
            # We've found our arr[k]!
            # Print the output
            if (seq == 3):
                print("Triplet: " + str(store_min) +
                    ", " + str(max_seq) + ", " +
                            str(nums[i]))
                
                return
            max_seq = nums[i]   
    # No triplet found
    print("No such triplet found", end = '')