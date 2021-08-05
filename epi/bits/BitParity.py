def parity(x: int) -> int:
    '''
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >>  8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1
    '''
    num_bits = 0
    while x:
        num_bits ^= x & 1
        print(num_bits)
        print(x)
        x >>= 1
    return num_bits
parity(10)