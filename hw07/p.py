def filter_lst(fn,lst):  
    if lst==[]:
        return []
    elif fn(lst[0])==False:
        print (False)
        return filter_lst(fn, lst[1:])
    else:
        print (True)
        return [lst[0]] + filter_lst(fn, lst[1:])
    

def even(x):
    if x%2==0:
        return True
    else:
        return False

filter_lst(even,[1,2,3,4])
   