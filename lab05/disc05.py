from lab05 import *


def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max([height(b) for b in branches(t)])


def max_path_sum(t):
    """Return the maximum path sum of the tree
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    return label(t) + max([max_path_sum(b) for b in branches(t)])


def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,[tree(2,[tree(3),tree(4)]),tree(5,[tree(6,[tree(7)]),tree(8)])])
    >>> print_tree(square_tree(numbers))
    """
    # this row can't be put in the return statement because it creates nested lists.
    new_branches=[square_tree(b) for b in branches(t)]
    return tree(label(t)*label(t),new_branches)


def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10)  # returns None
    """
    if label(tree)==x:
        return [label(tree)]
    for b in branches(tree):
        path=find_path(b, x)
        if path:
            return [label(tree)] + path


       
        
        





            
    
            
   


               
         
        
       









t = tree(1,[tree(3,[tree(4),tree(5),tree(6)]),tree(2)])


g=[1, [2, [4, [6], [1], [2]], [5, [6], [1], [2]]], [3, [4, [6], [1], [2]], [5, [6, [1], [2]], [1], [2]]]]
