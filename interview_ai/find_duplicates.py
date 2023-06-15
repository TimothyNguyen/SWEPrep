def find_duplicates(nums):
    num_frequency = {}
    duplicates = []

    # Loop through the input list and update the frequency in the hashmap
    for num in nums:
        # Update the frequency of the current number in the hashmap
        # TODO: Update the code here
        num_frequency[num] = num_frequency.get(num, 0) + 1


    # Check the frequency of each number and add duplicates to the output list
    for num, frequency in num_frequency.items():
        # Check if the number appears more than once
        # TODO: Update the code here
        if frequency > 1:
            duplicates.append(num)

    # Return the list of duplicates
    return duplicates