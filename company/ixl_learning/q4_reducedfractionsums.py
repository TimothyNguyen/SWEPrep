'''
Consider two fractions in the form a/b and c/d where a, b, c, and d are integers.

Give a string describing an arithmetic expression that sums these two 
fractions in the form: a/b + c/d, compute the sum and fully reduce the 
resultant fraction to its simplest form.

For example,

The expression 1/2 + 1/6 evaluates to 4/6, which we reduce to the string 2/3.

The expression 7/10 + 13/10 evaluates to 20/10, which reduce to the string 2/1.

Complete the function reducedFractionSums in the editor below. The function must 
return an array of strings representing the fully reduced fractions.

reducedFractionSums has the following parameter(s): 
expression[expressions[0], ..., expressions[n-1]] : an array of strings 
in the form a/b+c/d.
'''
import fractions

def reducedFractionSums(expressions):
    """
    Fairly self-explanatory, just use the built-in fractions package to perform
    the fraction addition -- they'll be automatically reduced in the end.
    """
    sum_array = []
    for expr in expressions:
        first_frac_string, second_frac_string = expr.split('+')
        first_frac = fractions.Fraction(first_frac_string)
        second_frac = fractions.Fraction(second_frac_string)
        sum_frac = first_frac + second_frac
        sum_array.append(str(sum_frac.numerator) + '/' + str(sum_frac.denominator))

    return sum_array