class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_to_str_array = [str(num) for num in nums]
        num_to_str_array.sort(key = lambda x: x * 10, reverse=True)
        while len(num_to_str_array) > 1 and num_to_str_array[0] == '0':
            num_to_str_array = num_to_str_array[1:]
        largest_number = ''.join(num_to_str_array)
        return largest_number