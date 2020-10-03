def multiply(m, n):
    """>>> multiply(5, 3)
    15
    """
    mi= min(m,n)
    ma= max(m,n) 
    if  mi == 0:
        return 0
    

    return ma + multiply(ma,mi-1)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    
    
    if n == 1:
        return 1 
    
    #print(steps)
    if n % 2 == 0:  
        
        return hailstone(n//2)+1
    else:
        #print((n*3)+1)
        return hailstone((n*3)+1)+1

def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """
    if n1==0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 < n2 % 10:
        return merge(n1 // 10, n2) * 10 + n1 % 10
    else:
        return merge(n1, n2 // 10) * 10 + n2 % 10



def return_same(n):
    
    left,right=n//10,n%10
    print(f'left:{left}')
    print(f'right:{right}')
    if left<=0:
        return n     
        
    return return_same(left)*10+right

def return_order(n):

    left,right=n//10,n%10

    if left==0:
        return n
    
    if right>left%10:
        right,left=left%10,left-left%10+right
        print(f'left:{left}')
        print(f'right:{right}')
        n=left*10+right
        print(f'n:{n}')
    elif right<left%10:
        print(f'left:{left}')
        print(f'right:{right}')
        n=left*10+right
        print(f'n:{n}')
    return return_order(n//10)*10+right


    
        

     
    
    # return return_order(left)*10+right
    



def is_prime(n):
    def prime_helper(index):
        if index==1:
            return True
        elif n%index==0 or n==1:
            return False
        else:
            return  prime_helper(index-1)
    return prime_helper(n-1)
    

def missing_digits(n):
    # this is working perfectly but ok doctest didn't accept
    left,right=n//10,n%10
    # print(f'right:{right}, left:{left}')
    if left==0:
        return 0
    
    elif right-left%10> 1:
        # print('called')
        # print(f'right:{right}, left:{left}') 
        return missing_digits((n//10)*10+(right-1))+1
    else:
        return missing_digits(n//10)

    
    
