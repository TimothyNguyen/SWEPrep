'''
data = [
  ("Whole Foods", 48.11, 5),
  ("Comcast", 89.99, 10),
  ("Comcast", 89.99, 20),
  ("Comcast", 89.99, 30),
  ("T-Mobile", 40.00, 45),
  ("T-Mobile", 40.00, 55),
  ("T-Mobile", 40.33, 65),
  ("Jetblue", 20.11, 80),
  ("Jetblue", 20.11, 90),
  ("Jetblue", 20.11, 95),
]
-> [ “Comcast” ]

Question:
Each line represents a COMPANY, AMOUNT, DAY
Return a list of companies which are "persistent".

For this problem, a "persistent" company means:

There are 3+ transactions with the same company, same price, 
and the same interval of time b/w transaction
A company is not "persistent" if any one of the transactions:

Is at a diff interval from the rest, ex Jetblue
Is a diff price from the rest, ex. T-Mobile
Is not in a set of 3+, ex. Whole Foods
Context:
I've gotten variations of this question at 3 different fintech companies. 
Parsing / filtering data from logs or streams. It's worth preparing for. 
It's not about algorithmic complexity (O(n)), rather clean / 
well structured / readable code.
'''
import collections
class Solution:
    def persistentCompanies(self, logs):
        data = collections.defaultdict(list)
        for name, price, day in logs:
            data[name].append((price, logs))
        
        def is_persistent(company, val):
            if len(val) < 3: return False
            price = val[0][0]
            day = val[1][1] - val[0][1]

            for i in range(1, len(val)):
                if price != val[i][0] or day != val[i][1] - val[i-1][1]:
                    return False
            return True


        output = []
        for company in data:
            val = data[company]
            if is_persistent(company, val):
                output.append(company)
        return output

s = Solution()
data = [("Whole Foods", 48.11, 5),("Comcast", 89.99, 10),("Comcast", 89.99, 20),("Comcast", 89.99, 30),("T-Mobile", 40.00, 45),("T-Mobile", 40.00, 55),("T-Mobile", 40.33, 65),("Jetblue", 20.11, 80),("Jetblue", 20.11, 90),("Jetblue", 20.11, 95)]
print(s.persistentCompanies(data))
