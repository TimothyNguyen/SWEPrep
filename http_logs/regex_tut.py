import re

# Write a Python program to check that a string contains 
# only a certain set of characters (in this case a-z, A-Z and 0-9).
s = "ABCDEFabcdef123450"
one = re.search(r'[a-zA-Z0-9]+', s)
print(one)

# Write a Python program that matches a string that has an a followed 
# by zero or more b's.
s = "abbbb"
print(re.search(r'a(b*)$', s))

# Write a Python program that matches a string that has an a followed by one or more b's
s = "a"
print(re.search(r'a(b+)$', s))

# Write a Python program to find sequences of lowercase letters joined with a underscore
print(re.findall(r'([a-z]+_[a-z]+)$', "a_basdf"))
# print(re.findall(r'^[a-z]+_[a-z]+$', "a_basdf"))