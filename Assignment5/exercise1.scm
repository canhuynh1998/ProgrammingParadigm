; CS152 Fall 2022 
; Hoc Can Huynh
; 014836757
; Homework assignment 5 
; Exercise 1


(define linear 
    (lambda (m x b)
        (+ (* m x) b)
    )
)

(define quadratic 
    (lambda (a x b c)
        (+ (* a (expt x 2) ) (* b x) c )
    )
)

(define chooseMapping 
    ( lambda (flag list_number)
      (cond 
        ((equal? flag "linear") ( map (lambda(x)(linear 5 x 3)) list_number))
        ((equal? flag "quadratic") ( map (lambda(x)(quadratic 3 x 4 1)) list_number))
        )
    )
)

(display (chooseMapping "linear" '(1 2 3 4 5 6 7 8 9 10)))
(newline)
(display (chooseMapping "quadratic" '(1 2 3 4 5 6 7 8 9 10)))
(newline)

