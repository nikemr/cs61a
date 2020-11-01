my_list=[1,2,4,5,6,7]
def linked_list(my_list):
    if my_list:
        inner=my_list[0]
        return  [inner, linked_list(my_list[1:])]
    else: 
        return []
        
     
    


