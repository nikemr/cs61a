scheme_eval(Pair('+', Pair(2, Pair(2, nil))), create_global_frame())

expr = read_line('(+ (+ 2 2) (+ 1 3) (* 1 4))')
scheme_eval(expr, create_global_frame()) # Type SchemeError if you think this errors

expr = read_line('(yolo)')
scheme_eval(expr, create_global_frame()) 