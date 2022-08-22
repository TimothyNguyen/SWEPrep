class Solution:
    def minSwaps(self, data: List[int]) -> int:
        sum_of_ones = sum(data)
        prefix_sum = 0
        for i in range(sum_of_ones):
            prefix_sum += data[i]
        ans = prefix_sum
        for i in range(sum_of_ones, len(data)):
            prefix_sum -= data[i - sum_of_ones]
            prefix_sum += data[i]
            ans = max(ans, prefix_sum)
        return sum_of_ones - ans