my_list=[1,2,4,5,6,7]
def linked_list(my_list):
    
    if my_list:
        first=my_list[0]
        so_far= [first, linked_list(my_list[1:])]
        # print(so_far)
        return  so_far
    else: 
        return []
        

n=124464564
def recursive_linked_list(n):
    full=[]
    linked_one=[]

    while n>0:
        full.insert(0,n%10)
        n=n//10
    return linked_list(full)


n=124464564
def higher_linked_list(n):
    full=[]    

    while n>0:
        full.insert(0,n%10)
        n=n//10

    def linked_list(my_list):
        
        if my_list:
            first=my_list[0]
            return  [first, linked_list(my_list[1:])]
        else: 
            return []

    return linked_list(full)