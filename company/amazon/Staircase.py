def count_ways(n):
  if n < 2:
    return 1
  if n == 2:
    return 2
  
  n1, n2, n3 = 1, 1, 2
  for i in range(3, n+1):
    n1, n2, n3 = n2, n3, n1+n2+n3
  return n3


def main():

  print(count_ways(3))
  print(count_ways(4))
  print(count_ways(5))


main()
