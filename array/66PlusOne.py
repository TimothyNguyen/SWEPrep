def plusOne(digits):
    carry = 1
    for i in reversed(range(digits)):
        if digits[i] + carry > 9:
            digits[i] = 0
            carry = 1
        else:
            digits[i] += carry
            carry = 0
    if carry == 1: digits.push(0, 1)
    return digits