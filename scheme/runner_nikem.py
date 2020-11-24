from scheme import *
global_frame = create_global_frame()
formals = Pair('a', Pair('b', Pair('c', nil)))
vals = Pair(1, Pair(2, Pair(3, nil)))
frame = global_frame.make_child_frame(formals, vals)
global_frame.lookup('a') # Type SchemeError if you think this errors