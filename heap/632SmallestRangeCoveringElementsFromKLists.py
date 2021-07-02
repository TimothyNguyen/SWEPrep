def smallestRange(nums):
    # Put elements of the list in a min heap
    # we need to store the number, corresponding row 
    # for that number, and index in row for that number
    heap = [(row[0], i, 0) for i, row in enumerate(nums)]   
    heapq.heapify(heap) # Creates heap

    # Best interval so far by finding range
    best_interval = (float("-inf"), float("inf"))

    # Get max
    curr_max = max(row[0] for row in nums)

    # While the heap isn't empty
    while heap:
        # Remove the number from the heap, use it as the new min
        curr_min, row_num, row_index = heapq.heappop(heap)

        # Calculate the new range and update if better
        if curr_max - curr_min < best_interval[1] - best_interval[0]:
            best_interval = (curr_min, curr_max)
        
        # If the min number has no neighbor elements in the list, end
        if row_index + 1 == len(nums[row_num]):
            return best_interval
        
        # Else:
        # Move one index down in te list and fetch the neighbor
        # Compare the new element: set new max to be this element if needed
        # Add to min heap
        new_elem = nums[row_num][row_index + 1]
        curr_max = max(curr_max, new_elem)
        heap.heappush(heap, (new_elem, row_num, row_index + 1))

