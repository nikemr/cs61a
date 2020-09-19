from doctest import testmod, run_docstring_examples

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    if k == 0:
        return 1
    
    fact = 1

    while k:
        fact= fact*n
        print(n)
        n = n-1               
        k -= 1

    return fact


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    summ=0
    if y<10:
        return y
    else:        
        while y>0:
            n=next_modulo(y)
            y = y//10
            summ+=n
        return summ

def next_modulo(y):
    return y%10    


testmod()
# for calling doctest for the file 'v' for verbose mode
# python3 -m doctest -v Lab01.py