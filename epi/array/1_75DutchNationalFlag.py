def dutch_flag_partition(pivot_idx: int, A: List[int]) -> None:
    pivot = A[pivot_idx]
    # Keep the following invariants during partitioning
    # bottom group: A[:smaller]
    # middle group: A[smaller:equal]
    # unclassified group: A[equal: larger]
    # Top group: A[larger:]
    smaller, equal, larger = 0, 0, len(A)
    # Keep iterating until there's an unclassified element
    while equal < larger:
        # A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else: 
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]