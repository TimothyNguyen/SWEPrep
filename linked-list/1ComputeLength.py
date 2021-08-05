# Iterate over the list until there are no more elements, incrementing a
# counter at each iteration.
def getLength(A):
    length = 0
    while A:
        A = A.next
        length += 1
    return length