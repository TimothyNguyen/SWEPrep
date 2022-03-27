class Solution:
   def solve(self, s):
      output = ""
      num=""
      for i in s:
         if i.isalpha():
            output+=i*int(num)
            num=""
         else:
            num+=i
      return output
ob = Solution() 
print(ob.solve("4B3A2D1C2B"))