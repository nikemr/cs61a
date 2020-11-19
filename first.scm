(define(repeat k fn)(if (> k 0)(begin (fn) (repeat (- k 1) fn))nil))
(repeat 5(lambda () (fd 100)(repeat 5(lambda () (fd 20) (rt 144)))(rt 144)))nil
