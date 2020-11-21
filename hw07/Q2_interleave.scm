(define (interleave first second)
      (if (or (null? first) (null? second))
          (append first second)
          
          (cons (car first) (cons (car second) (interleave (cdr first) (cdr second)))
      
)))



(interleave (list 1 3 5) (list 2 4 6))

; expect (1 2 3 4 5 6)



(interleave (list 1 3 5) nil)

; expect (1 3 5)



(interleave (list 1 3 5) (list 2 4))

; expect (1 2 3 4 5)