from math import *
def find_bitwise_complement(num):
  
    # Write your code here
    # your code will replace this placeholder return statement
    if num == 0:
        return 1

    bit_count = floor(log2(num)) + 1
    all_bits_set = floor(pow(2, bit_count)) - 1
    '''
   0111111
    101010
-> 0010101
    '''
    # print(all_bits_set)
    # print(bit_count)
    return all_bits_set ^ num
