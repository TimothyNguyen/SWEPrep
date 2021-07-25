class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1, n+1):
            temp = ""
            if i % 3 == 0 and i % 5 == 0: temp += "FizzBuzz"
            elif i % 3 == 0: temp += "Fizz"
            elif i % 5 == 0: temp += "Buzz"
            else: temp += str(i)
            ans.append(temp)
        return ans
            
            